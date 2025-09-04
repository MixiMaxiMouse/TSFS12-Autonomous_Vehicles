classdef (Abstract) PurePursuitControllerBase < ControllerBase
    properties
        plt_car_point;
        plt_car_path;
        plt_pursuit_horizon;
        plt_pursuit_point;
        pursuit_point_fig;
        animate_pure_pursuit;
    end
    methods
        function obj = PurePursuitControllerBase(pursuit_point_fig)
            obj = obj@ControllerBase();
            if nargin < 1 || pursuit_point_fig == false
                obj.animate_pure_pursuit = false;
            else
                obj.animate_pure_pursuit = true;
                figure(pursuit_point_fig);
                hold on
                obj.plt_car_point = plot(0, 0, 'o', 'MarkerFaceColor','r', 'MarkerEdgeColor','r');
                obj.plt_pursuit_point = plot([0, 0], [0, 0], 'o', 'MarkerFaceColor','b', 'MarkerEdgeColor','b');
                obj.plt_car_path = plot([0, 0], [0, 0], 'k');
                obj.plt_pursuit_horizon = plot([0, 0], [0, 0], 'k--');
                hold off
            end
        end

        function pursuit_plot(obj, p_car, p_purepursuit)
            if obj.animate_pure_pursuit
                set(obj.plt_car_point, 'XData', p_car(1), 'YData', p_car(2));
                if all(obj.plt_car_path.XData == 0)
                    set(obj.plt_car_path, 'XData', [p_car(1), p_car(1)],...
                        'YData', [p_car(2), p_car(2)])
                else
                    set(obj.plt_car_path, 'XData', [obj.plt_car_path.XData, p_car(1)],...
                        'YData', [obj.plt_car_path.YData, p_car(2)])
                end
                phi = linspace(0, 2 * pi, 40);
                set(obj.plt_pursuit_horizon, 'XData', cos(phi) * obj.l + p_car(1),...
                        'YData', sin(phi) * obj.l + p_car(2));
                set(obj.plt_pursuit_point, 'XData', p_purepursuit(1),...
                    'YData', p_purepursuit(2));
                pause(0.01);
            end
        end
    end
end


%         def _pursuit_plot(self, p_car, p_purepursuit):
%         "Helper function to illustrate pursuit-point selection"
% 
%         if self._pp_fig:  # Is pursuit-point illustration activated?
%             self._car_point[0].set_data([p_car[0]], [p_car[1]])  # Move car
%             self._pursuit_point[0].set_data(
%                 [p_purepursuit[0]], [p_purepursuit[1]]
%             )  # Move pursuit-point
%             phi = np.linspace(0, 2 * np.pi, 40)
%             self._pursuit_horizon[0].set_data(
%                 np.cos(phi) * self.l + p_car[0], np.sin(phi) * self.l + p_car[1]
%             )  # Horizon circle
%             dd = self._car_path[0].get_data()
%             self._car_path[0].set_data(
%                 (np.hstack((dd[0], [p_car[0]])), np.hstack((dd[1], [p_car[1]])))
%             )  # Travelled path
% 
%             # Update plot
%             self._pp_fig.canvas.draw()
%             self._pp_fig.canvas.flush_events()


