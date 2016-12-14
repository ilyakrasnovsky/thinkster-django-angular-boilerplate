/**
* Register controller
* @namespace thinkster.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.authentication.controllers') //module name for this controller
    .controller('RegisterController', RegisterController); //instead of factory, attach controller called RegisterController to this module

  //inject dependencies (services) including Authentication in authentication.service.js
  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register; //allows the template in the html to access the register method defined below

    /**
    * @name register
    * @desc Register a new user
    * @memberOf thinkster.authentication.controllers.RegisterController
    */
    function register() {
      //calls the register method from the Authentication service we defined
      Authentication.register(vm.email, vm.password, vm.username);
    }
  }
})();