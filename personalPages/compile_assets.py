import sass 
import os

SASS_DIR='sass'
CSS_OUTPUT_DIR='static/personalPages/css/'

# sass
sass.compile(dirname=(SASS_DIR, CSS_OUTPUT_DIR), output_style='compressed')