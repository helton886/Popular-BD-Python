from datetime import date, timedelta
import random
import MySQLdb
from pyUFbr.baseuf import ufbr
import string

db = MySQLdb.connect(user="root",passwd="root",db="voacampeao",port=3306,host="localhost", autocommit=False) #Conexão com servidor
print("conectou")

#Inserir

pessoas = ["Camila","Elivelton","Helton","Thiago","Joao","Maria","Elisangela","Camilinha","Thiaguinho","Eliveltinho",
           "Heltinho","Mariazinha","Joaozinho", "Andreza","Andrezinha","Lucas","Luquinhas","Allan","Allanzinho","Elinaldo"]

cidades = ufbr.list_uf

descricao = ["Ganhar esse premio seria como um sonho realizado",
             "Venho treinando há anos, me ajude a conseguir",
             "Sou Bicampeã na modalidade, me ajude a chegar ao tricampeonato",
             "Meu maior objetivo é conquistar minha primeira medalha",
             "Treino Karatê desde os 12 anos, estou em busca da minha 10 medalha na modalidade"]


modalidade = ["Corrida",
              "Natação",
              "Salto com vara",
              "Triatlo",
              "Cem metros rasos",
              "Maratona",
              "Judô",
              "Karatê",
              "Taekwondo",
              "Ginástica Ritmica",
              "Trampolim Acrobático",
              "Esgrima",
              "Tiro com Arco",
              "Luta Olímpica",
              "Boxe"]

competicao = ["São Silvestre",
              "50m Livres",
              "Campeonato Regional de Atletismo",
              "Ironman",
              "Cem metros rasos",
              "São Carlos Tadeu",
              "Olimpíadas Regional",
              "Olimpíadas Regional",
              "Olimpiadas Regional",
              "Comp Ginástica",
              "Comp Ginástica",
              "Nacional Olimpic",
              "Nacional Olimpic",
              "Nacional Olimpic",
              "Lutinha"]

# enum patrocinio : `status` enum('1','2','3','4')

# enum viagem :  `status` enum('1','2','3','4','5')

# sexo enum('M','F','N')

#realizando transação

def randomString(stringLength=6):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


cursor = db.cursor()
usuario = 10
try:
    db.begin()
    dataida = date(2019,5,13)
    datavolta = date(2019, 6, 1)
    dataagr = date.today()
    ticket = randomString()
    for x in range(290):
        status_viagem = str(random.randint (1,5))
        rand = random.randint(0,14)
        while rand == 2:
            rand = random.randint(0,14)
        print(rand)
        usuariostr = str(usuario)
        print("'%s','%s','%s','%s','%s','%s','%s','%s','%s'" % (random.choice(cidades),random.choice(cidades),dataida,datavolta,random.choice(descricao),modalidade[rand],status_viagem,competicao[rand],usuariostr))

        cursor.execute("INSERT INTO viagem (origem,destino,data_ida,data_volta,descricao_comp,modalidade_comp,status,competicao,idUsuario) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (random.choice(cidades),
                        random.choice(cidades),dataida,datavolta,random.choice(descricao),modalidade[rand],status_viagem,competicao[rand],usuariostr))

        if (status_viagem == '4' or status_viagem == '3'):
            print("teste")
            status_pat = ''
            meuint = random.randint(1,6)
            datapatrocinio = dataida - timedelta(days=3)

            cursor.execute("SELECT * FROM viagem")
            tuplaViagem = cursor.fetchall()
            lastindex = len(tuplaViagem) - 1
            viagemID = tuplaViagem[lastindex][0]
            usuariostrPat = str(usuario + 1)

            if status_viagem == "4" :
                status_pat = '3'
            else:
                status_pat = str(random.randint(1,2))
                if status_pat == '1':
                    ticket = ''
            print("%s','%s','%s','%s','%s'" % (datapatrocinio, status_pat, ticket, viagemID, usuariostrPat))
            print("teste2")
            cursor.execute("INSERT INTO patrocinio (data_intencao,status,ticket,idViagem,idUsuario) VALUES ('%s','%s','%s','%s','%s')" % (
                datapatrocinio, status_pat,ticket,viagemID, usuariostrPat))
        dataida = dataida + timedelta(days=9)
        datavolta = datavolta + timedelta(days=9)
        usuario += 1
        ticket = randomString()
    db.commit()
except:
    print("deu erro")
    db.rollback()

#receber a última insserção


#como a pesquisa é singular, basta retornar apenas um item.
# cursor.execute("SELECT * FROM cliente where idcliente=1")
# print(cursor.fetchone())

#retorna os 10 primeiros items
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchmany(10))

# #atualizar
# cursor.execute("update cliente set nome='Ana' where idcliente=1")
#
# #remover
# cursor.execute("delete from cliente WHERE idcliente=2")

#Captura todos os dados novos
cursor.execute("SELECT * FROM viagem")
print(cursor.fetchall())


db.close() #fechar conexão
print("conexão fechada")
