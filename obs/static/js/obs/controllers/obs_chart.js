angular.module('opal.controllers').controller(
    'ObsChartCtrl',
    function($scope, $timeout, $modalInstance, episode){
        $scope.episode = episode;

        $scope.chart = function(selector, columns){
            var chart = c3.generate({
                bindto: selector,
                data: {
                    x: 'x',
                    columns: columns
                },
                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            fit: true
                        }
                    },
                    y: {
                        label: { // This pushes the axes across and fixes
                            // #12 for now.
                            // TODO: Investigate how to do this betterer !
                            text: ' ',
                            position: 'outer-middle'
                        }
                    }
                }
            });

            return chart
        };

        $scope.render_charts = function(){
            var x = ['x']
            var bp_systolic  = ['Systolic'];
            var bp_diastolic = ['Diastolic'];
            var pulse        = ['Pulse'];
            var resp_rate    = ['Respiratory Rate'];
            var sp02         = ['Sp02'];
            var temp         = ['Temperature'];
            var height       = ['Height'];
            var weight       = ['Weight'];

            _.map($scope.episode.observation, function(ob){
                if(!_.isDate(ob.datetime)){
                    ob.datetime = moment(ob.datetime)._d;
                }

                x.push(ob.datetime);
                bp_systolic.push(ob.bp_systolic);
                bp_diastolic.push(ob.bp_diastolic);
                pulse.push(ob.pulse);
                resp_rate.push(ob.resp_rate);
                sp02.push(ob.sp02);
                temp.push(ob.temperature);
                height.push(ob.height);
                weight.push(ob.weight);
            });

            var bp_chart = $scope.chart('#bp_chart', [x, bp_systolic, bp_diastolic]);
            var pulse_chart = $scope.chart('#pulse_chart', [x, pulse]);
            var resp_chart = $scope.chart('#resp_rate_chart', [x, resp_rate]);
            var sp02_chart = $scope.chart('#sp02_chart', [x, sp02]);
            var temp_chart = $scope.chart('#temperature_chart', [x, temp]);
            var hw_chart = $scope.chart('#height_weight_chart', [x, height, weight]);

        };

        $timeout($scope.render_charts, 500);

        //
        // Sensible bindings for cancelling our modal
        //
	$scope.cancel = function() {
	    $modalInstance.close('cancel');
	};

    });
