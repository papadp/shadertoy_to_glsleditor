import re
import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: %s <file_path>" % sys.argv[0])
        sys.exit()


    shadertoy_file_path = sys.argv[1]

    with open(shadertoy_file_path, "r") as h:

        file_content = h.read()

    glsl_editor_content = '''#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;
#define iResolution u_resolution
#define iTime u_time
'''

    file_content = re.sub(".*?void +?mainImage.*?\(.*?\)", "void main()", file_content)
    file_content = file_content.replace("fragCoord", "gl_FragCoord")
    file_content = file_content.replace("fragColor", "gl_FragColor")

    # print(glsl_editor_content)

    # print("=================================================================")

    glsl_editor_content += file_content

    # print(glsl_editor_content)

    with open("out.frag", "w") as h:
        h.write(glsl_editor_content)


if __name__ == "__main__":
    main()