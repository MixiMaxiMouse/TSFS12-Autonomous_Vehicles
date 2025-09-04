close all
clear
close all
% add casadi to path using addpath

%% Optimize trajectory
L = 1.5;        % Wheel base (m)
v = 15;         % Constant velocity (m/s)
u_max = pi/4;   % Maximum steering angle (rad)

N = 75; % Number of elements
nx = 3; % Degree of state vector
Nc = 3; % Degree of interpolation polynomials

state_i = [0; 0; 0];
state_f = [3; 1; 0];

opti = casadi.Opti();  % Create optimizer

% Define optimization variables and motion equations
x = casadi.MX.sym('x', nx);
u = casadi.MX.sym('u');

f = casadi.Function('f',{x, u},...
    {v * cos(x(3)), v * sin(x(3)), v * tan(u) / L});

X = opti.variable(nx, N + 1);
pos_x = X(1, :);
pos_y = X(2, :);
ang_th = X(3, :);

U = opti.variable(N, 1);
T = opti.variable(1);

% Set the element length (with final time T unknown, and thus an 
% optimization variable)
dt = T / N;

% Set initial guess values of variables
opti.set_initial(T, 0.1);
opti.set_initial(U, 0.0 * ones(N, 1));
opti.set_initial(pos_x, linspace(state_i(1), state_f(1), N + 1));
opti.set_initial(pos_y, linspace(state_i(2), state_f(2), N + 1));

% Define collocation parameters
tau = casadi.collocation_points(Nc, 'radau');
[C, ~] = casadi.collocation_interpolators(tau);

% Formulate collocation constraints
for k = 1:N  % Loop over elements
    Xc = opti.variable(nx, Nc);
    X_kc = [X(:, k) Xc];
    for j = 1:Nc
        % Make sure that the motion equations are satisfied at
        % all collocation points
        [f_1, f_2, f_3] = f(Xc(:, j), U(k));
        opti.subject_to(X_kc*C{j+1}' == dt*[f_1; f_2; f_3]);
    end
    % Continuity constraints for states between elements
    opti.subject_to(X_kc(:, Nc + 1) == X(:, k + 1));
end

% Input constraints
for k = 1:N
    opti.subject_to(-u_max <= U(k) <= u_max);
end

% Initial and terminal constraints
opti.subject_to(T >= 0.001);
opti.subject_to(X(:, 1) == state_i);
opti.subject_to(X(:, end) == state_f);

% Formulate the cost function
alpha = 1e-2;
opti.minimize(T + alpha*sumsqr(U));

% Choose solver ipopt and solve the problem
opti.solver('ipopt', struct('expand', true), struct('tol', 1e-8));
sol = opti.solve();

% Extract solution trajectories and store them in the mprim variable
pos_x_opt = sol.value(pos_x);
pos_y_opt = sol.value(pos_y);
ang_th_opt = sol.value(ang_th);
u_opt = sol.value(U);
T_opt = sol.value(T);
dt_opt = sol.value(dt);
tt = (0:dt_opt:T_opt - dt_opt);

%% Plot results
figure(10)
plot(pos_x_opt, pos_y_opt)
title(sprintf("T=%.2f s", T_opt));
xlabel('x [m]')
ylabel('x [m]')
box off

figure(11)
plot(tt, u_opt * 180 / pi)
hold on
plot(tt, 0 * tt + u_max * 180 / pi, 'k--')
plot(tt, 0 * tt - u_max * 180 / pi, 'k--')
hold off
xlabel("t [s]")
ylabel("steer [deg]")
box off

