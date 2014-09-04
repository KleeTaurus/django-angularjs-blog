'use strict'

angular.module('blogpost', ['ngCookies', 'blogService']).
    run(['$http', '$cookies',
        function($http, $cookies) {
            $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
            $http.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
        }
    ]);
