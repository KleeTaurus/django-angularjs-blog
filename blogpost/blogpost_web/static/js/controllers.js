'use strict'

function BlogResourceCtl($scope, BlogResource) {
    $scope.blogs = []

    BlogResource.query(function(response) {
        $scope.blogs = response;
    });

    $scope.createBlog = function() {
        var blog = new BlogResource();
        blog.title = $scope.blog_title;
        blog.content = $scope.blog_content;
        blog.$save(function(response) {
            $scope.blogs.unshift(response);
            $scope.blog_title = "";
            $scope.blog_content = "";

            toastr.info('You have create a new blog successfully.');
        });

    };

    $scope.deleteBlog = function(blog_list) {
        blog_list.$delete(function(response) {
            var index = $scope.blogs.indexOf(blog_list);
            $scope.blogs.splice(index, 1);
        });
    };
}
