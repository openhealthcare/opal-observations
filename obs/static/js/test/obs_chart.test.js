describe('Dummy', function(){
    "use strict";

    var $scope, $httpBackend, $modalInstance;
    var controller;
    var episode = {observation: [{}]};

    beforeEach(module('opal.controllers'));

    beforeEach(inject(function($injector){
        var $rootScope   = $injector.get('$rootScope');
        var $controller  = $injector.get('$controller');
        var $modal       = $injector.get('$modal');
        $scope           = $rootScope.$new();
        $httpBackend     = $injector.get('$httpBackend');

        $modalInstance = $modal.open({template: 'Not a real template'});

        controller = $controller('ObsChartCtrl', {
            $scope        : $scope,
            $modalInstance: $modalInstance,
            episode       : episode
        });
    }));

    describe('chart()', function() {
        it('should do a thing', function(){
            var chart = $scope.chart('body', [1,2,3]);
            expect(chart.element.toString()).toEqual('[object HTMLBodyElement]');
        });
    });

    describe('render_charts', function() {
        it('should render the chart', function() {
            var today = new Date(2002, 2, 29);
            jasmine.clock().mockDate(today);
            spyOn($scope, 'chart');
            $scope.render_charts()
            expect($scope.chart).toHaveBeenCalledWith(
                '#height_weight_chart', [
                    ['x', today], ['Height', undefined], ['Weight', undefined]])
        });
    });

    describe('cancel()', function(){
        it('should close with null', function(){
            spyOn($modalInstance, 'close');
            $scope.cancel();
            expect($modalInstance.close).toHaveBeenCalledWith('cancel');
        });
    });


})
