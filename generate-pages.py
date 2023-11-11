import json

def criar_html(postagens):
    with open('templates/index.html', 'w', encoding='utf-8') as arquivo_html:
        arquivo_html.write('<html>\n<head>\n<title>Postagens</title>\n<link rel="stylesheet" href="static/style.css">\n<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">\n</head>\n<body>\n')

        for postagem in postagens:
            arquivo_html.write('<div>\n')
            arquivo_html.write(f'<h2>{postagem["titulo"]}</h2>\n')
            arquivo_html.write(f'<p>Autor: {postagem["autor"]}</p>\n')
            arquivo_html.write(f'<p>{postagem["descricao"]}</p>\n')
            arquivo_html.write('</div>\n\n')

        arquivo_html.write('</body>\n</html>')
        arquivo_html.write('<a href="https://lms.ada.tech/student/projects/by-module-id/eace9e5a-ac86-4e19-983c-cac20736dad4/by-project-submission-id/8be5d499-8ac2-47e0-86ff-8ce6e210d20b" type="button" class="btn btn-outline-success">Link Projeto</a>')

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)

arquivo_json = 'posts.json'
dados = ler_json(arquivo_json)
criar_html(dados)
print(f'Arquivo HTML gerado com sucesso: index.html')