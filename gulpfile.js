const gulp = require("gulp")

const css = () =>{
    const postCSS = require("gulp-postcss");
    const sass = require("gulp-sass");
    const minify = require("gulp-csso");
    sass.compiler = require("node-sass");
    return gulp.src("assets/scss/styles.scss").pipe(sass().on("error", sass.logError)).pipe(postCSS([require("tailwindcss"),require("autoprefixer")])).pipe(minify()).pipe(gulp.dest("static/css"))
};

exports.default = css;

/* #19.1 */
/* assets/scss/styles.scss가 기본적으로 있고, sass로 pipe하고, postCSS로도 작업하고, postCSS가 이해하는 두가지 플러그인은 tailwindcss와 autoprefixer가 있고, */
/* 이게 끝나고나면 모든 아웃풋을 minify할꺼고 그이후 결과물을 static/css안에 넣겠다 라는 말임. */

/* 이게 끝나면. => styles.scss에 tailwind를 추가할 수 있다. */