function dxdt = single_integrator(t, x, u, mdlpar)
% System-model function
%     
% Input arguments are:
%   t - time 
%   x - state vector of the agent (position) 
%   u - the control input u, 
%   mdlpar - structure with parameters of the model 
%     
% Output:
%   dxdt - state-derivative

    dxdt = u;
end
