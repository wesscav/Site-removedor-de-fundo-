from rembg import remove 
from PIL import Image 
import io
from IPython.display import display

imagem = Image.open('imagens\teste.jpg')
#teste sa
#tratamento da imagem:

#rotacao da imagem
def rotacao_imagem(graus, imagem):
    return imagem.rotate(graus)

#mudanca de dimensoes
def mud_dimensoes(nova_largura, nova_altura):
    return imagem.resize((nova_largura, nova_altura))

#remover o fundo

#transformar a imagem para bytes
buffer = io.BytesIO()
imagem.save(buffer, format="PNG")
input_data = buffer.getvalue()
#removendo o fundo
output_data = remove(input_data)

# Reconvertendo para uma imagem do PIL
imagem_fundo_removido = Image.open(io.BytesIO(output_data))
imagem_fundo_removido.save("imagem_fundo_removido.png")
display(imagem_fundo_removido)

