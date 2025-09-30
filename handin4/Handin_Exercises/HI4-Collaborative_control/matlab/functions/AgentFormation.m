classdef AgentFormation < handle
    properties
        n
        n_agents
        agents
        formation_references
        agent_idx
        measurement_graph
        absolute_measurement
    end
    methods
        function obj = AgentFormation(agents, G, formation_refs, n)
            obj.n = n;
            obj.n_agents = numel(agents);
            obj.agents = agents;
            obj.formation_references = formation_refs;
            obj.agent_idx = reshape((1:(obj.n_agents * obj.n)), ...
                obj.n, obj.n_agents)';

            obj.absolute_measurement = zeros(1, obj.n_agents, 'logical');
            for a_i=1:obj.n_agents
                edg = {};
                for idx=1:numel(G)
                    if (numel(G{idx}) == 1 && G{idx}(1) == a_i) || ...
                       (numel(G{idx}) == 2 && G{idx}(2) == a_i)
                        edg{end + 1} = G{idx};
                    end
                end
                if numel(edg) == 1 && (numel(edg{1}) == 1)
                    obj.absolute_measurement(a_i) = true;
                    obj.measurement_graph{end + 1} = obj.agent_idx(edg{1}(1), :);
                else
                    meas_idx_ai = {};
                    for k=1:numel(edg)
                        meas_idx_ai{end + 1} = [obj.agent_idx(edg{k}(1), :); obj.agent_idx(edg{k}(2), :)];
                    end
                    obj.measurement_graph{end + 1} = meas_idx_ai;
                end
            end
        end

        function y = h_state(~, x, meas_idx)
            y = x(meas_idx);
        end

        function y = h_relative(~, x, meas_idx)
            for i = 1:numel(meas_idx)
                y(i, :) = x(meas_idx{i}(1, :)) - x(meas_idx{i}(2, :));
            end
        end

        function dxdt = ode(obj, t, x)
            xr = reshape(x, obj.n, []);
            dxdt =[];
            
            for i = 1:obj.n_agents
                if obj.absolute_measurement(i)
                    y = obj.h_state(x, obj.measurement_graph{i});
                else
                    y = obj.h_relative(x, obj.measurement_graph{i});
                end                
                u = obj.agents(i).g(y, obj.formation_references{i}(t), obj.agents(i).ctrlpar);
                dxidt = obj.agents(i).f(t, xr(:,i), u, obj.agents(i).mdlpar);
                dxdt =  [dxdt; dxidt];
            end            
        end
    end
end