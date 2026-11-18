# Demos fictícias com identidade própria (nomes inventados). Executado dentro de gerar.py.
LOGO_BASE = '.logo.livre{margin-top:.4rem}'

hubs['restaurante'] = {
  'nome': 'Cantina Bella Nonna', 'titulo': 'Cantina Bella Nonna', 'sub': 'Cucina di famiglia',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@500;600&family=Yellowtail&family=Cormorant+Garamond:ital,wght@1,600&display=swap',
  'disp': '"Cormorant Garamond",Georgia,serif',
  'cores': {'bg': '#120b08', 'fg': '#f6eedf', 'mut': 'rgba(246,238,223,.64)', 'acc': '#d9502f', 'acc2': '#a8361c', 'accfg': '#fff7ea', 'line': 'rgba(246,238,223,.16)'},
  'logo': {'forma': 'livre', 'temNome': True, 'html': '<div class="lg-nonna"><span class="a">Cantina</span><span class="b">Bella Nonna</span><span class="c"><i></i>dal 1998<i></i></span></div>'},
  'css': LOGO_BASE + """
.lg-nonna{display:flex;flex-direction:column;align-items:center;color:#f6eedf;padding:.4rem 1rem}
.lg-nonna .a{font:600 .95rem Oswald,sans-serif;letter-spacing:.55em;margin-right:-.55em;text-transform:uppercase;display:flex;align-items:center;gap:.8rem}
.lg-nonna .a:before,.lg-nonna .a:after{content:"";width:2rem;height:2px;background:#d9502f}
.lg-nonna .b{font:400 4.4rem/1 Yellowtail,cursive;white-space:nowrap;margin:.15rem 0 .1rem;text-shadow:0 6px 24px rgba(0,0,0,.6);transform:rotate(-4deg)}
.lg-nonna .c{font:600 .8rem Oswald,sans-serif;letter-spacing:.4em;margin-right:-.4em;text-transform:uppercase;color:#e9b44c;display:flex;align-items:center;gap:.6rem}
.lg-nonna .c i{width:.45rem;height:.45rem;background:#d9502f;transform:rotate(45deg)}""",
  'fundo': {'svg': D['bistroBg'].replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1), 'veu': 'linear-gradient(180deg,rgba(18,11,8,.3),rgba(18,11,8,.75) 45%,rgba(12,7,5,.97))'},
  'status': {'expediente': {0: [11.5, 16], 2: [11.5, 23], 3: [11.5, 23], 4: [11.5, 23], 5: [11.5, 23.9], 6: [11.5, 23.9]}},
  'whatsapp': NODUS_WA,
  'principal': {'tipo': 'cardapio', 'rotulo': 'Cardápio Digital', 'sub': 'Monte o pedido e envie pelo WhatsApp', 'icone': 'livro'},
  'acoes': [
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Gostou? Conta pra gente', 'aviso': AVISO_GOOGLE},
    {'tipo': 'whatsapp', 'rotulo': 'WhatsApp', 'sub': 'Reservas e aniversários'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Prato do dia e novidades', 'url': NODUS_IG},
  ],
  'wifi': {'rede': 'BellaNonna_Clientes', 'senha': 'mangia2026'},
  'info': {'endereco': 'Rua Treze de Maio, 412 · Centro', 'horario': 'Ter a sáb 11h30 às 23h · Dom 11h30 às 16h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=cantina+italiana'},
  'cardapio': [
    {'cat': 'Antipasti', 'itens': [
      {'n': 'Bruschetta da Nonna', 'd': 'Pão italiano tostado, tomate, manjericão, alho e azeite. 4 unidades.', 'p': 32},
      {'n': 'Polpettine al Sugo', 'd': 'Almôndegas da casa no molho de tomate, com parmesão e pão.', 'p': 42, 'tag': 'Mais pedido'},
      {'n': 'Burrata com Tomate Confit', 'd': 'Burrata cremosa, tomatinhos confitados, pesto e torradas.', 'p': 58},
      {'n': 'Carpaccio Classico', 'd': 'Lâminas de filé, alcaparras, parmesão, rúcula e molho de mostarda.', 'p': 48}]},
    {'cat': 'Massas', 'itens': [
      {'n': 'Spaghetti alla Carbonara', 'd': 'Guanciale, gema, pecorino e pimenta-do-reino. Sem creme de leite.', 'p': 62, 'tag': 'Receita da Nonna'},
      {'n': 'Lasanha à Bolonhesa', 'd': 'Massa fresca, ragu de carne cozido por 6 horas, bechamel e queijo gratinado.', 'p': 58},
      {'n': 'Fettuccine Alfredo com Frango', 'd': 'Molho de manteiga e parmesão com frango grelhado.', 'p': 59},
      {'n': 'Nhoque ao Sugo', 'd': 'Nhoque de batata feito na casa, molho de tomate italiano e manjericão.', 'p': 52},
      {'n': 'Ravioli de Queijo', 'd': 'Recheio de ricota e muçarela de búfala, manteiga e sálvia.', 'p': 64}]},
    {'cat': 'Pizzas', 'itens': [
      {'n': 'Margherita', 'd': 'Molho de tomate, muçarela, tomate e manjericão. 8 pedaços.', 'p': 69},
      {'n': 'Calabresa', 'd': 'Calabresa artesanal, cebola roxa e azeitonas. 8 pedaços.', 'p': 72},
      {'n': 'Quatro Queijos', 'd': 'Muçarela, gorgonzola, parmesão e catupiry. 8 pedaços.', 'p': 79},
      {'n': 'Parma com Rúcula', 'd': 'Presunto parma, rúcula, tomate seco e lascas de parmesão. 8 pedaços.', 'p': 89}]},
    {'cat': 'Sobremesas', 'itens': [
      {'n': 'Tiramisù', 'd': 'Biscoito champagne, café espresso, mascarpone e cacau.', 'p': 28, 'tag': 'Mais pedido'},
      {'n': 'Cannoli Siciliano', 'd': '2 unidades recheadas com creme de ricota e pistache.', 'p': 24},
      {'n': 'Panna Cotta', 'd': 'Creme de baunilha com calda de frutas vermelhas.', 'p': 26}]},
    {'cat': 'Bebidas', 'itens': [
      {'n': 'Taça de Vinho da Casa', 'd': 'Tinto ou branco, 150 ml.', 'p': 24},
      {'n': 'Chianti DOCG', 'd': 'Garrafa 750 ml. Tinto italiano, ótimo com massas ao sugo.', 'p': 129},
      {'n': 'Suco Natural', 'd': 'Laranja, limão ou abacaxi com hortelã. 400 ml.', 'p': 12},
      {'n': 'Refrigerante Lata', 'd': '350 ml.', 'p': 7},
      {'n': 'Água com ou sem Gás', 'd': '500 ml.', 'p': 5}]},
  ],
}

hubs['oficina'].update({
  'nome': 'Garage 77 Auto Center', 'titulo': 'Garage 77 Auto Center', 'sub': 'Mecânica • Injeção • Freios • Suspensão',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Oswald:wght@500;600&family=Anton&display=swap',
  'logo': {'forma': 'livre', 'temNome': True, 'html': '<div class="lg-g77"><span class="s"><i></i><i></i><i></i></span><span class="g">GARAGE<b>77</b></span><span class="a">Auto Center</span></div>'},
  'css': LOGO_BASE + """
.lg-g77{display:flex;flex-direction:column;align-items:center;color:#fff;transform:skewX(-8deg)}
.lg-g77 .s{display:flex;gap:.35rem;margin-bottom:.5rem}.lg-g77 .s i{width:2.6rem;height:.4rem;background:#F59E0B}.lg-g77 .s i:nth-child(2){background:#fff}.lg-g77 .s i:nth-child(3){background:#EA580C}
.lg-g77 .g{font:400 3.9rem/.9 Anton,Impact,sans-serif;letter-spacing:.02em;display:flex;align-items:center;gap:.5rem;text-shadow:0 8px 24px rgba(0,0,0,.6)}
.lg-g77 .g b{font-weight:400;background:#F59E0B;color:#111;padding:.05em .18em;border-radius:.25rem}
.lg-g77 .a{font:600 .95rem Oswald,sans-serif;letter-spacing:.6em;margin-right:-.6em;text-transform:uppercase;margin-top:.55rem;color:#d4d4d8}""",
  'acoes': [
    {'tipo': 'whatsapp', 'rotulo': 'Orçamento no WhatsApp', 'sub': 'Mande a placa e o problema', 'mensagem': 'Olá, Garage 77! Vim pelo hub e gostaria de um orçamento.'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Antes e depois dos serviços', 'url': NODUS_IG},
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Ajude outros motoristas', 'aviso': AVISO_GOOGLE},
  ],
  'info': {'endereco': 'Av. Brasil, 770 · Centro', 'horario': 'Seg a sex 08h às 18h · Sáb 08h às 12h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=auto+center'},
  'status': {'expediente': {1: [8, 18], 2: [8, 18], 3: [8, 18], 4: [8, 18], 5: [8, 18], 6: [8, 12]}},
})
hubs['oficina']['agenda']['servicos'] = [
  {'nome': 'Troca de óleo e filtros', 'desc': 'Óleo e filtros conforme o manual', 'tempo': '40 min', 'min': 40, 'icone': 'gota'},
  {'nome': 'Alinhamento e balanceamento', 'desc': 'Alinhamento 3D computadorizado', 'tempo': '1 h', 'min': 60, 'icone': 'roda'},
  {'nome': 'Revisão preventiva', 'desc': 'Checklist de 40 itens', 'tempo': '2 h', 'min': 120, 'icone': 'lista'},
  {'nome': 'Freios', 'desc': 'Pastilhas, discos e fluido', 'tempo': '1 h 30', 'min': 90, 'icone': 'freio'},
  {'nome': 'Suspensão', 'desc': 'Amortecedores, buchas e terminais', 'tempo': '2 h', 'min': 120, 'icone': 'chave'},
  {'nome': 'Diagnóstico com scanner', 'desc': 'Luz de injeção acesa? Começa aqui', 'tempo': '30 min', 'min': 30, 'icone': 'scan'},
  {'nome': 'Ar-condicionado', 'desc': 'Higienização e recarga de gás', 'tempo': '1 h', 'min': 60, 'icone': 'neve'},
]
hubs['oficina']['agenda']['horarios'] = {'semana': ['08:00', '09:00', '10:00', '11:00', '13:30', '14:30', '15:30', '16:30'], 'sabado': ['08:00', '09:00', '10:00', '11:00']}

hubs['loja'].update({
  'nome': 'Ateliê Lis', 'titulo': 'Ateliê Lis · Moda feminina', 'sub': 'Moda feminina',
  'fontes': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,500;1,500;1,600&display=swap',
  'disp': '"Cormorant Garamond",Georgia,serif',
  'cores': {'bg': '#140e12', 'fg': '#fbf3ef', 'mut': 'rgba(251,243,239,.62)', 'acc': '#e7b3a3', 'acc2': '#c98b79', 'accfg': '#2a1418', 'line': 'rgba(251,243,239,.14)'},
  'logo': {'forma': 'livre', 'temNome': True, 'html': '<div class="lg-lis"><svg viewBox="0 0 40 44" aria-hidden="true"><path d="M20 3c4 6 5 12 0 20-5-8-4-14 0-20zM20 23c3-6 9-9 16-8-2 7-8 11-16 8zM20 23c-3-6-9-9-16-8 2 7 8 11 16 8zM14 30h12M20 23v18" fill="none" stroke="#e7b3a3" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="a">Ateliê</span><span class="b">Lis</span></div>'},
  'css': LOGO_BASE + """
.lg-lis{display:flex;flex-direction:column;align-items:center;color:#fbf3ef}
.lg-lis svg{width:2.6rem;height:2.9rem;margin-bottom:.35rem}
.lg-lis .a{font:500 .85rem Inter,sans-serif;letter-spacing:.6em;margin-right:-.6em;text-transform:uppercase;color:#e7b3a3}
.lg-lis .b{font:italic 500 5.2rem/.9 "Cormorant Garamond",Georgia,serif;letter-spacing:.02em}""",
  'fundo': {'veu': 'radial-gradient(80% 50% at 20% 0%,rgba(231,179,163,.22),transparent 70%),radial-gradient(70% 45% at 100% 35%,rgba(160,90,130,.18),transparent 70%)'},
  'acoes': [
    {'tipo': 'whatsapp', 'rotulo': 'Atendimento no WhatsApp', 'sub': 'Tamanhos, trocas e entregas', 'mensagem': 'Olá, Ateliê Lis! Vim pelo hub.'},
    {'tipo': 'instagram', 'rotulo': 'Instagram', 'sub': 'Looks e lançamentos', 'url': NODUS_IG},
    {'tipo': 'google', 'rotulo': 'Avalie no Google', 'sub': 'Conte como foi sua compra', 'aviso': AVISO_GOOGLE},
  ],
  'info': {'endereco': 'Rua das Flores, 155 · Centro', 'horario': 'Seg a sex 09h às 19h · Sáb 09h às 14h', 'mapa': 'https://www.google.com/maps/search/?api=1&query=loja+de+roupas+femininas'},
  'status': {'expediente': {1: [9, 19], 2: [9, 19], 3: [9, 19], 4: [9, 19], 5: [9, 19], 6: [9, 14]}},
})

# ── Boteco Tijuca: cardápio em vídeo de demonstração (vídeos do Backyard, Juiz de Fora, usados com autorização) ──
hubs['tijuca']['principal'] = {'tipo': 'cardapio', 'rotulo': 'Cardápio Digital', 'sub': 'Veja cada prato em vídeo', 'icone': 'chopp', 'titulo': 'Cardápio'}
hubs['tijuca']['cardapioPedido'] = False
hubs['tijuca']['cardapioNota'] = 'Toque na foto para ver o prato em vídeo. Para pedir, chame o garçom.'
hubs['tijuca']['cardapio'] = [{'cat': c['cat'], 'itens': [{k: v for k, v in i.items() if k in ('n', 'p', 'd', 'v', 'op', 'm', 'desde')} for i in c['itens']]} for c in D['videos']]

# Demos fictícias: sem contato real da Nodus por enquanto
for k in ('restaurante', 'oficina', 'loja'):
    for a in hubs[k]['acoes']:
        if a['tipo'] == 'instagram' and not a.get('url'):
            a['aviso'] = 'No hub do seu negócio, este botão abre o Instagram da empresa.'
