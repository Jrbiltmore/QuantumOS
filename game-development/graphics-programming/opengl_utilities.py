import OpenGL.GL as gl
import OpenGL.GL.shaders as shaders
import numpy as np

class OpenGLUtilities:
    @staticmethod
    def initialize_shader(vertex_code, fragment_code):
        vertex_shader = shaders.compileShader(vertex_code, gl.GL_VERTEX_SHADER)
        fragment_shader = shaders.compileShader(fragment_code, gl.GL_FRAGMENT_SHADER)
        shader_program = shaders.compileProgram(vertex_shader, fragment_shader)
        return shader_program

    @staticmethod
    def create_vao(data):
        vao_id = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(vao_id)
        vbo_id = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo_id)
        array_type = (gl.GLfloat * len(data))
        gl.glBufferData(gl.GL_ARRAY_BUFFER, len(data) * 4, array_type(*data), gl.GL_STATIC_DRAW)
        return vao_id, vbo_id

    @staticmethod
    def draw_triangle(vao_id, shader_program):
        gl.glUseProgram(shader_program)
        gl.glBindVertexArray(vao_id)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

# Example Usage

vertex_shader_code = """
#version 330 core
layout (location = 0) in vec3 position;
void main() {
    gl_Position = vec4(position.x, position.y, position.z, 1.0);
}
"""

fragment_shader_code = """
#version 330 core
out vec4 FragColor;
void main() {
    FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
"""

triangle_data = [
    -0.5, -0.5, 0.0,
     0.5, -0.5, 0.0,
     0.0,  0.5, 0.0,
]

if __name__ == "__main__":
    # These operations would typically be part of a larger OpenGL application,
    # where a context is created using a library like GLFW or PySDL2.
    shader_program = OpenGLUtilities.initialize_shader(vertex_shader_code, fragment_shader_code)
    vao_id, _ = OpenGLUtilities.create_vao(triangle_data)
    # OpenGLUtilities.draw_triangle(vao_id, shader_program)
    # The draw operation should be called within the render loop of your OpenGL context.
