'use strict'

angular.module('blogService', ['ngResource']).
    factory('BlogResource', function($resource) {
        return $resource('api/blogs/:blog_id', {
            blog_id: '@id'
        }, {
            save: {
                method: 'POST',
                isArray: false
            },
            query: {
                method: 'GET',
                isArray: true
            },
            update: {
                method: 'PUT',
                isArray: false
            },
            destroy: {
                method: 'DELETE',
                isArray: false
            }
        });
    });
