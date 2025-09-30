close all
clear all
clc
addpath functions

%% Model, controllers, and agent formation
% A first example are 4 agents, all modeled by a single integrator, 
% and all measuring their absolute position. The controller for each 
% agent is a proportional controller.

% Now, formulate the formation graph and position references. 
% The graph is specified by a set of edges. An edge (i, j) represents 
% that agent j meausures the distance from agent i. If agent i measures 
% its own absolute position, this is represented by a tuple with element 
% i as (i,) and this is the case for all agents in this example.
n = 2;  % number of states is 2 (x, y)
G = {[1,], ... % Agent 1
     [2,], ... % Agent 2
     [3,], ... % Agent 3
     [4,], ... % Agent 4
     };

formation_references = {
    @(t) [cos(2*t), sin(2*t)]'; % Moving counter-clockwise on a circle 1
    @(t) [2*cos(-t), 2*sin(-t)]'; % Moving clockwaise on a circle with radius 2
    @(t) [3, 2]'; % Fixed position
    @(t) [5, 4]'; % Fixed position
};

%% Create all agents by assigning model and controller using 
%  CreateAgent and then form the formation using AgentFormation by
%  providing the references.
modelparam.m = 1;
controlparam1.k = 1;
controlparam2.k = 10;

agent = [
    CreateAgent(@single_integrator, modelparam, @g_absolute, controlparam2), ...
    CreateAgent(@single_integrator, modelparam, @g_absolute, controlparam1), ...
    CreateAgent(@single_integrator, modelparam, @g_absolute, controlparam1), ...
    CreateAgent(@single_integrator, modelparam, @g_absolute, controlparam2), ...
];

formation = AgentFormation(agent, G, formation_references, n);

%% Simulate
% Define an initial state and evaluate the formatation 
% state-transition function
x0 = [1, 0, 2, 0, 3, 0, 4, 0]'; % Initial values of the state vector.
formation.ode(0, x0);

% Simulate
tspan = 0:0.05:20; % Time vector for the simulation
[t,x] = ode23t(@formation.ode, tspan, x0);

%% Animate the results
figure(10)
clf
axis([-2 6 -3 6])
xlabel('x')
ylabel('y')
title('Example 0')
hold on
pd = cell(numel(agent), 1);  % Create empty plot handles for agents
for idx=1:numel(agent)
    pd{idx} = plot(nan, nan, 'o', ...
        'MarkerEdgeColor', 'b', 'MarkerFaceColor','b');
end
tstring = text(-1, 5, "");

for i=1:length(t)
    tstring.String = sprintf("t = %.1f", t(i));
    for idx=1:numel(agent)
        p = x(i, (idx - 1) * n + 1:(idx - 1) * n + 2);
        pd{idx}.XData = p(1);
        pd{idx}.YData = p(2);
    end
    pause(0.005);  % Adjust to preference
end
