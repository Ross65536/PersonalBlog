import sass 
import os

# sass
SASS_DIR='css/sass'
CSS_OUTPUT_DIR='static/personalPages/css/'
sass.compile(dirname=(SASS_DIR, CSS_OUTPUT_DIR), output_style='compressed')