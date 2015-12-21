var gulp = require('gulp')
var sass = require('gulp-sass')

gulp.task('compile-sass', function() {
    return gulp.src('wagtailfontawesome/static_src/wagtailfontawesome/scss/**/*.scss')
        .pipe(sass({
            includePaths: ['node_modules'],
        }))
        .pipe(gulp.dest('wagtailfontawesome/static/wagtailfontawesome/css'))
})

gulp.task('copy-fonts', function() {
    return gulp.src('node_modules/font-awesome/fonts/**/*')
        .pipe(gulp.dest('wagtailfontawesome/static/wagtailfontawesome/fonts'))
})

gulp.task('default', ['compile-sass', 'copy-fonts'])
