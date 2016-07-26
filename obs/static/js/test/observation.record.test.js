describe('Antimicrobial', function(){
  "use strict";

  var $routeParams;
  var Observation;

  beforeEach(function(){
      module('opal.services');
      module('opal.records');
      inject(function($injector){
          Observation = $injector.get('Observation');
          $routeParams  = $injector.get('$routeParams');
      });
  });

  describe("it should set observation defaults", function(){
    it("should set the observation datetime if its not set", function(){
      var observation = Observation({});
      expect(moment.isMoment(observation.datetime)).toBe(true);
    });

    it("should set the Observation datetime if it is set", function(){
      var observation = Observation({id: 1});
      expect(observation.datetime).toBe(undefined);
    });
  });
});
