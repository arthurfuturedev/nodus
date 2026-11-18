"""Gera os hubs da Nodus a partir do modelo padrão (base.html) + a configuração de cada cliente."""
import base64, json, sys, os
S = sys.argv[1]; H = S + '/hub'; OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
base = open(H + '/base.html', encoding='utf-8').read()
D = json.load(open(H + '/dados.json', encoding='utf-8'))
def uri(f, mime): return f'data:{mime};base64,' + base64.b64encode(open(H + '/img/' + f, 'rb').read()).decode()
def svguri(svg): return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()
NODUS_WA = ''; NODUS_IG = ''
AVISO_GOOGLE = 'No hub do seu negócio, este botão abre direto a avaliação no Google.'

hubs = {}

# ── Boteco Tijuca (cliente real) ──
hubs['tijuca'] = {
  'nome': 'Boteco Tijuca', 'titulo': 'Boteco Tijuca · Mogi Guaçu', 'sub': 'Mogi Guaçu • SP',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@500;600;700&display=swap',
  'disp': 'Oswald,"Arial Narrow",Impact,sans-serif',
  'cores': {'bg': '#05170d', 'fg': '#f4ead3', 'mut': 'rgba(244,234,211,.68)', 'acc': '#d4571a', 'acc2': '#a83f0f', 'accfg': '#f4ead3', 'line': 'rgba(244,234,211,.18)'},
  'logo': {'src': uri('logo-tijuca.jpg', 'image/jpeg'), 'temNome': True},
  'fundo': {'src': uri('fundo-tijuca.jpg', 'image/jpeg'), 'blur': 4, 'veu': 'radial-gradient(120% 70% at 50% 15%,rgba(5,23,13,0),rgba(5,23,13,.5) 72%),linear-gradient(180deg,rgba(5,23,13,.15),rgba(5,23,13,.6) 40%,rgba(4,16,9,.93))'},
  'status': {'sempreAberto': True},
  'whatsapp': '5519998378153',
  'principal': {'tipo': 'link', 'rotulo': 'Cardápio Digital', 'sub': 'Pratos, petiscos e bebidas', 'icone': 'chopp', 'link': '', 'aviso': 'O cardápio digital do Tijuca entra no ar em breve.'},
  'acoes': [
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Leva menos de 1 minuto', 'url': 'https://search.google.com/local/writereview?placeid=ChIJYbY3AeZXyJQRQKDsxdC44Og'},
    {'tipo': 'whatsapp', 'rotulo': 'WhatsApp', 'sub': 'Reservas e aniversários'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Música ao vivo e novidades', 'url': 'https://www.instagram.com/botecotijuca/'},
  ],
  'wifi': {'rede': 'tijucaclientes', 'senha': '@Tijucaclientes11'},
}

# ── Jhow's Barbearia (cliente real) ──
hubs['jhows'] = {
  'nome': "Jhow's Barbearia", 'titulo': "Jhow's Barbearia", 'sub': 'Estilo é atitude',
  'fontes': 'https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap',
  'disp': 'Anton,Impact,"Arial Narrow",sans-serif', 'raio': '.7rem', 'estilo': 'street',
  'cores': {'bg': '#070707', 'fg': '#f5f5f5', 'mut': 'rgba(245,245,245,.62)', 'acc': '#f5f5f5', 'acc2': '#c9c9c9', 'accfg': '#0a0a0a', 'line': 'rgba(255,255,255,.16)'},
  'logo': {'src': uri('jhows-logo.png', 'image/png'), 'forma': 'livre', 'largura': '10.5rem', 'temNome': True},
  'fundo': {'src': uri('jhows-equipe.jpg', 'image/jpeg'), 'modo': 'capa', 'topo': '10.4rem', 'veu': 'linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.6) 70%,#070707)'},
  'espaco': '16.5rem',
  'status': {'expediente': {0: [9, 15], 1: [9, 20.5], 2: [9, 20.5], 3: [9, 20.5], 4: [9, 20.5], 5: [9, 17]}},
  'whatsapp': '5515996534206', 'mesa': False,
  'principal': {'tipo': 'agenda', 'rotulo': 'Agendar horário', 'sub': 'Escolha o barbeiro e o horário', 'icone': 'scis', 'titulo': 'Agendar'},
  'acoes': [
    {'tipo': 'whatsapp', 'rotulo': 'WhatsApp', 'sub': 'Dúvidas sobre o seu horário', 'mensagem': 'Olá, gostaria de tirar uma dúvida sobre meu agendamento na Jhows Barbearia'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': '@jhows_barbearia_', 'url': 'https://www.instagram.com/jhows_barbearia_/'},
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Nota 5.0 com mais de 10 mil cortes', 'url': 'https://www.google.com/maps/search/?api=1&query=Jhow%27s+Barbearia+Engenheiro+Coelho'},
  ],
  'planos': {'titulo': 'O Clube', 'sub': 'Pague uma vez por mês, venha quando precisar', 'itens': [
    {'nome': 'Bronze', 'preco': 70, 'inclui': ['2 cortes', '1 sobrancelha']},
    {'nome': 'Prata I', 'preco': 130, 'inclui': ['4 cortes', '2 sobrancelhas']},
    {'nome': 'Prata II', 'preco': 140, 'inclui': ['2 cortes', '2 sobrancelhas', '2 barbas']},
    {'nome': 'Ouro I', 'preco': 200, 'inclui': ['4 cortes', '2 sobrancelhas', '1 limpeza de pele']},
  ]},
  'info': {'endereco': 'No UNASP · Estr. Mun. Pastor Walter Boger, Engenheiro Coelho - SP', 'horario': 'Seg a qui 09h às 20h30 · Sex 09h às 17h · Dom 09h às 15h · Sáb fechado',
           'mapa': 'https://www.google.com/maps/search/?api=1&query=UNASP+Engenheiro+Coelho'},
  'agenda': {
    'servicos': [
      {'nome': 'Corte de cabelo', 'desc': 'Técnicas modernas e clássicas', 'tempo': '30 min', 'min': 30, 'preco': 45, 'icone': 'scis'},
      {'nome': 'Barba', 'desc': 'Com toalha quente', 'tempo': '20 min', 'min': 20, 'preco': 35, 'icone': 'razor'},
      {'nome': 'Sobrancelha', 'desc': 'Design e limpeza', 'tempo': '10 min', 'min': 10, 'preco': 20, 'icone': 'brow'},
      {'nome': 'Limpeza de pele', 'desc': 'Tratamento facial completo', 'tempo': '45 min', 'min': 45, 'preco': 80, 'icone': 'gota'},
    ],
    'profissionais': ["Jhow's", 'Quaresma', 'Nicolas', 'Deivid'],
    'simularOcupados': False,
    'horarios': {
      'semana': ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00'],
      'porDia': {0: ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '13:30', '14:00', '14:30'],
                 5: ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']}},
    'expediente': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1},
    'campoExtra': 'Referência do corte (opcional)', 'rotuloExtra': 'Referência',
  },
}

# ── Bistrô Lumière (demo fictícia de restaurante) ──
hubs['restaurante'] = {
  'nome': 'Bistrô Lumière', 'titulo': 'Bistrô Lumière', 'sub': 'Cozinha autoral',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap',
  'disp': '"Playfair Display",Georgia,serif',
  'cores': {'bg': '#0a0807', 'fg': '#f5f2ea', 'mut': 'rgba(245,242,234,.62)', 'acc': '#D4AF37', 'acc2': '#a88a2a', 'accfg': '#111', 'line': 'rgba(212,175,55,.26)'},
  'logo': {'src': svguri(D['cloche'].replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1)), 'forma': 'livre', 'largura': '13rem'},
  'fundo': {'svg': D['bistroBg'].replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1), 'veu': 'linear-gradient(180deg,rgba(8,5,6,.35),rgba(8,5,6,.72) 45%,rgba(5,4,4,.96))'},
  'status': {'sempreAberto': True},
  'whatsapp': NODUS_WA,
  'principal': {'tipo': 'cardapio', 'rotulo': 'Cardápio Digital', 'sub': 'Monte o pedido e envie pelo WhatsApp', 'icone': 'livro'},
  'acoes': [
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Sua opinião nos ajuda a melhorar', 'aviso': AVISO_GOOGLE},
    {'tipo': 'whatsapp', 'rotulo': 'WhatsApp', 'sub': 'Reservas e eventos'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Pratos da semana', 'url': NODUS_IG},
  ],
  'wifi': {'rede': 'Lumiere_Clientes', 'senha': 'bonappetit2026'},
  'info': {'endereco': 'Rua das Acácias, 88 · Centro', 'horario': 'Ter a dom · 12h às 15h e 19h às 23h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=bistr%C3%B4'},
  'cardapio': [{'cat': c['cat'], 'itens': [{'n': i['n'], 'd': i['d'], 'p': i['p'], **({'tag': i.get('tag') or 'Mais pedido'} if i.get('top') else {})} for i in c['items']]} for c in D['menu']],
}

# ── Apex Centro Automotivo (demo fictícia de oficina) ──
ic_of = {'oil': 'gota', 'wheel': 'roda', 'list': 'lista', 'brake': 'freio', 'scan': 'scan', 'snow': 'neve'}
logo_apex = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" fill="#111114"/><path d="M57 31a2 2 0 0 0 0 2.8l3.2 3.2a2 2 0 0 0 2.8 0l7.5-7.5a12 12 0 0 1-15.9 15.9L40.8 59.2a4.2 4.2 0 0 1-6-6l13.8-13.8a12 12 0 0 1 15.9-15.9z" fill="none" stroke="#F59E0B" stroke-width="3.4" stroke-linejoin="round"/></svg>'
hubs['oficina'] = {
  'nome': 'Apex Centro Automotivo', 'titulo': 'Apex Centro Automotivo', 'sub': 'Mecânica • Injeção • Freios • Suspensão',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@500;600&display=swap',
  'disp': 'Oswald,"Arial Narrow",Impact,sans-serif',
  'cores': {'bg': '#09090B', 'fg': '#ffffff', 'mut': '#A1A1AA', 'acc': '#F59E0B', 'acc2': '#EA580C', 'accfg': '#111', 'line': 'rgba(255,255,255,.12)'},
  'logo': {'src': svguri(logo_apex)},
  'fundo': {'svg': D['cena'], 'veu': 'linear-gradient(180deg,rgba(9,9,11,.78),rgba(24,24,27,.9))'},
  'status': {'sempreAberto': True},
  'whatsapp': NODUS_WA, 'mesa': False,
  'principal': {'tipo': 'agenda', 'rotulo': 'Agendar revisão', 'sub': 'Escolha o serviço, o dia e o horário', 'icone': 'cal', 'titulo': 'Agendar serviço'},
  'acoes': [
    {'tipo': 'whatsapp', 'rotulo': 'Orçamento no WhatsApp', 'sub': 'Resposta em poucos minutos', 'mensagem': 'Olá, Apex! Vim pelo hub e gostaria de um orçamento.'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Bastidores e entregas', 'url': NODUS_IG},
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Ajude outros motoristas', 'aviso': AVISO_GOOGLE},
  ],
  'info': {'endereco': 'Av. Brasil, 1500 · Centro', 'horario': 'Seg a sex 08h às 18h · Sáb 08h às 13h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=oficina+mec%C3%A2nica'},
  'agenda': {
    'rotuloServicos': 'Escolha os serviços',
    'servicos': [{'nome': s['nome'], 'tempo': s['tempo'], 'min': s['min'], 'icone': ic_of.get(s['icone'], 'chave')} for s in D['oficina']],
    'horarios': {'semana': ['08:00', '09:30', '11:00', '14:00', '15:30', '17:00'], 'sabado': ['08:00', '09:30', '11:00']},
    'expediente': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1},
    'campoExtra': 'Modelo e placa do carro (opcional)', 'rotuloExtra': 'Veículo',
  },
}

# ── Maison Aurora (demo fictícia de loja) ──
hubs['loja'] = {
  'nome': 'Maison Aurora', 'titulo': 'Maison Aurora', 'sub': 'Moda feminina autoral',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap',
  'disp': '"Playfair Display",Georgia,serif',
  'cores': {'bg': '#0D0D11', 'fg': '#ffffff', 'mut': 'rgba(255,255,255,.62)', 'acc': '#E5C158', 'acc2': '#b8902f', 'accfg': '#111', 'line': 'rgba(255,255,255,.12)'},
  'logo': {'texto': 'MA'},
  'fundo': {'veu': 'radial-gradient(80% 50% at 15% 0%,rgba(139,92,246,.28),transparent 70%),radial-gradient(70% 45% at 100% 30%,rgba(229,193,88,.16),transparent 70%)'},
  'status': {'sempreAberto': True},
  'whatsapp': NODUS_WA, 'mesa': False,
  'principal': {'tipo': 'catalogo', 'rotulo': 'Ver coleção', 'sub': f"{len(D['loja'])} peças · peça pelo WhatsApp", 'icone': 'sacola', 'titulo': 'Coleção Verão'},
  'acoes': [
    {'tipo': 'whatsapp', 'rotulo': 'Atendimento no WhatsApp', 'sub': 'Tamanhos, trocas e entregas', 'mensagem': 'Olá, Maison Aurora! Vim pelo hub.'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Looks e lançamentos', 'url': NODUS_IG},
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Conte como foi sua compra', 'aviso': AVISO_GOOGLE},
  ],
  'info': {'endereco': 'Shopping Center · Piso 1', 'horario': 'Seg a sáb 10h às 22h · Dom 14h às 20h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=loja+de+roupas'},
  'catalogo': {'tamanhos': 'P · M · G · GG', 'itens': [{'n': p[0], 'cat': p[1], 'p': p[2], 'd': p[3], 'arte': D['sp'][p[4]], **({'tag': 'Mais vendido'} if i == 0 else {})} for i, p in enumerate(D['loja'])]},
}


# ── Ateliê da Moda (cliente real · Mogi Guaçu) ──
_wa_atelie = '5519981618772'
hubs['atelie'] = {
  'nome': 'Ateliê da Moda', 'titulo': 'Ateliê da Moda · Mogi Guaçu', 'sub': 'Moda que valoriza mulheres reais',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,500&display=swap',
  'disp': '"Playfair Display",Georgia,serif',
  'cores': {'bg': '#160a0d', 'fg': '#fbf1ee', 'mut': 'rgba(251,241,238,.68)', 'acc': '#e3343b', 'acc2': '#a81c2a', 'accfg': '#ffffff', 'line': 'rgba(251,241,238,.17)'},
  'logo': {'src': uri('atelie-logo.jpg', 'image/jpeg'), 'forma': 'livre', 'largura': '9.6rem', 'temNome': True},
  'css': """
#logo.livre img{border-radius:50%;background:#fff;box-shadow:0 0 0 3px rgba(227,52,59,.6),0 0 0 9px rgba(227,52,59,.14),0 22px 50px rgba(0,0,0,.55)}

.hero .tag{text-transform:none;font:italic 500 1.22rem/1.35 "Playfair Display",Georgia,serif;letter-spacing:.01em;color:#fbf1ee;opacity:.92}""",
  'fundo': {'src': uri('atelie-fundo.jpg', 'image/jpeg'), 'blur': 6, 'pos': '50% 30%',
            'veu': 'radial-gradient(110% 60% at 50% 8%,rgba(22,10,13,.15),rgba(22,10,13,.62) 70%),linear-gradient(180deg,rgba(60,8,16,.35),rgba(22,10,13,.72) 42%,rgba(18,8,10,.95))'},
  'status': {'expediente': {1: [9.5, 18], 2: [9.5, 18], 3: [9.5, 18], 4: [9.5, 18], 5: [9.5, 18], 6: [9.5, 13]}},
  'destaques': ['Do 36 ao 52'],
  'whatsapp': _wa_atelie, 'mesa': False,
  'principal': {'tipo': 'link', 'rotulo': 'Comprar pelo WhatsApp', 'sub': 'Há 20 anos vestindo histórias', 'icone': 'wa',
                'link': 'https://wa.me/' + _wa_atelie + '?text=' + __import__('urllib.parse').parse.quote('Olá, Ateliê da Moda! Vim pelo hub e gostaria de ver as novidades.')},
  'acoes': [
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Conte como foi sua visita', 'url': 'https://search.google.com/local/writereview?placeid=ChIJ2W7yvNVXyJQRFZlr4FZSDHw'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': '@loja_ateliemoda · looks e provador', 'url': 'https://www.instagram.com/loja_ateliemoda/'},
    {'tipo': 'link', 'icone': 'wa', 'rotulo': 'Grupo VIP no WhatsApp', 'sub': 'Promoções em primeira mão', 'url': 'https://chat.whatsapp.com/KdxUSz1g3TC45iu76vsKUJ'},
  ],
  'info': {'endereco': 'R. Sérgio Sínico, 35 · Jd. Guaçu Mirim III, Mogi Guaçu', 'horario': 'Seg a sex 09h30 às 18h · Sáb 09h30 às 13h',
           'mapa': 'https://www.google.com/maps/search/?api=1&query=Ateli%C3%AA+da+Moda+R.+S%C3%A9rgio+S%C3%ADnico+35+Mogi+Gua%C3%A7u'},
}
exec(open(H + '/ficticias.py', encoding='utf-8').read())

# ── Relatório de acessos ──────────────────────────────────────────────
# Cole aqui o código de cada cliente (Google Analytics "G-..." e/ou Umami "id do site").
# Vazio = o hub funciona normalmente, só não registra acessos.
# Nas placas, grave o link com ?o=nfc (NFC) ou ?o=qr (QR code) para separar a origem.
ANALYTICS = {
    'tijuca': {'ga': '', 'umami': ''},
    'jhows':  {'ga': '', 'umami': ''},
}
for k, a in ANALYTICS.items():
    a = {c: v for c, v in a.items() if v}
    if a and k in hubs: hubs[k]['analytics'] = a

for k, cfg in hubs.items():
    html = base.replace('/*CONFIG*/{}', json.dumps(cfg, ensure_ascii=False))
    open(f'{OUT}/{k}.html', 'w', encoding='utf-8').write(html)
    print(k, round(len(html) / 1024), 'KB')
