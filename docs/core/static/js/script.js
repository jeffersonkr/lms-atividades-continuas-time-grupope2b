/* Verifica se a senha confirma, caso senhas diferentes evita submit mudando tipo do botao pra button*/
    var checa = function() {
        if (document.getElementById('senha').value == document.getElementById('senha2').value) {
            document.getElementById('senha').style.border = '3px rgba(0, 255, 0, 0.349) solid';
            document.getElementById('senha2').style.border = '3px rgba(0, 255, 0, 0.349) solid';
            document.getElementsByName('cadastrar')[0].type = 'submit';
            document.getElementById('mensagem').innerHTML = ''
        } else {
            document.getElementById('senha').style.border = '3px rgba(255, 0, 0, 0.349) solid';
            document.getElementById('senha2').style.border = '3px rgba(255, 0, 0, 0.349) solid';
            document.getElementById('mensagem').style.color = 'red';
            document.getElementById('mensagem').style.fontSize = '8px';
            document.getElementById('mensagem').style.textAlign = 'center';
            document.getElementById('mensagem').innerHTML = 'Senhas não conferem!'
            document.getElementsByName('cadastrar')[0].type = 'button';
        }
    }