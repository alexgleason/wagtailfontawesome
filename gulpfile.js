var gulp = require('gulp');
var sass = require('gulp-sass');
var sassUnicode = require('gulp-sass-unicode');
var cleanCSS = require('gulp-clean-css');
var gzip = require('gulp-gzip');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('compile-sass', function() {
    return gulp.src('wagtailfontawesome/static_src/wagtailfontawesome/scss/**/*.scss')
        .pipe(sass({
            includePaths: ['node_modules'],
	    outputStyle: 'compressed'
        }))
        .pipe(sassUnicode())
        .pipe(cleanCSS())
        .pipe(gulp.dest('wagtailfontawesome/static/wagtailfontawesome/css'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('wagtailfontawesome/static/wagtailfontawesome/css'));
});

gulp.task('copy-fonts', function() {
    return gulp.src('node_modules/font-awesome/fonts/**/*')
        .pipe(gulp.dest('wagtailfontawesome/static/wagtailfontawesome/fonts'));
});

gulp.task('default', ['compile-sass', 'copy-fonts']);
