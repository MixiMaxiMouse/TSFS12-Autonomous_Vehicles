clear
addpath Functions

%% Generate a path
car = SingleTrackModel();
car.controller = MiniController();
w0 = [0, 0, 0, 2];
[t, w, u] = car.simulate(w0, 40, 0.1);
M = 10;  % Path downsample factor
p = w(1:M:end, 1:2);

figure(10)
plot(p(:, 1), p(:, 2), 'rx')

%% Create path object
pl = SplinePath(p);
fprintf('Path length: %.2f m\n', pl.length);

%% Plot path and properties

s = linspace(0, pl.length, 200);

% Plot path
figure(20)
plot(pl.x(s), pl.y(s), 'b')

% Plot curvature
figure(21)
plot(s, pl.c(s))


% Get tangent and normal at point s0
s0 = 10;
[tangent, normal] = pl.heading(s0);

tangent
normal

L = 5;  % Tangent length
figure(22)
plot(pl.x(s), pl.y(s), 'b')
hold on
plot(pl.x(s0), pl.y(s0), 'ro')
plot([pl.x(s0) pl.x(s0)+L*tangent(1)], ...
    [pl.y(s0) pl.y(s0)+L*tangent(2)], 'k', 'linewidth', 2);
plot([pl.x(s0) pl.x(s0)+L*normal(1)], ...
    [pl.y(s0) pl.y(s0)+L*normal(2)], 'r', 'linewidth', 2);
hold off

%% Projection
% Plot the path and a possible current position of the vehicle
p0 = [17, 15];
figure(23)
plot(pl.x(s), pl.y(s), 'b')
hold on
plot(p0(1), p0(2), 'ko')
hold off

% Project onto the path at around s=50
[s_p, d_p] = pl.project(p0, 50, 1, 20);
disp(s_p)
disp(d_p)
fprintf("Projection point at %.2f m, position (%.2f, %.2f), %.2f m from " + ...
        "point (%.2f, %.2f).\n", s_p, pl.x(s_p), pl.y(s_p), d_p, ...
        p0(1), p0(2));

% Visualize the projection. Experiment with different starting points.
%s_0 = 70;
s_0 = 20;
[s_proj, ~] = pl.project(p0, s_0, 1, 20);
figure(24)
plot(pl.x(s), pl.y(s), 'b')
hold on
plot(p0(1), p0(2), 'ko')
plot(pl.x(s_proj), pl.y(s_proj), 'ro')
plot([p0(1), pl.x(s_proj)], [p0(2), pl.y(s_proj)], 'k--')
hold off

