"""Static pages and home-service UX for La Vita Spa; loaded by build.py.
Site owners: confirm that travelling visits are offered before publishing city pages.
"""
from html import escape

CITY={
 'sousse':{
  'fr':{
   'name':'Sousse','lead':'À Sousse et Sahloul, demandez un massage bien-être chez vous. Précisez votre quartier pour vérifier la faisabilité du déplacement.',
   'h1':'Massage à domicile <em>Sousse.</em>',
   'h2':'À Sousse : la détente à votre adresse, sur demande',
   'intro':'La Vita Spa accueille ses visiteurs Rue Pakistan à Sahloul. Si vous préférez une prestation à domicile, indiquez votre lieu de rendez-vous pour connaître les possibilités de déplacement. La disponibilité d’un professionnel n’est jamais automatique.',
   'h3':'Sahloul, Khezama, Hammam Sousse : quel quartier indiquer ?',
   'zones':'Décrivez le secteur où vous résidez, que ce soit Sahloul, Khezama, Hammam Sousse, le centre-ville ou ailleurs dans la région. Ces quartiers sont des exemples pour faciliter votre demande, et non une garantie de couverture. L’équipe vous précisera si un déplacement est possible.',
   'h4':'Bien préparer son massage chez soi',
   'prep':'Choisissez un endroit calme et accessible. Lors de votre prise de contact, demandez si du matériel est nécessaire, la durée de la séance, le prix total, les frais de déplacement éventuels et les modalités de confirmation. La réservation n’est effective qu’après accord du spa.',
   'extra':'Vous préférez venir sur place ? Retrouvez les <a href="/massage-sousse/">massages au spa à Sahloul</a>, ainsi que le hammam individuel et les soins du visage, sur rendez-vous.',
   'q':[('Intervenez-vous à Sahloul et Hammam Sousse ?','Adressez-nous votre quartier et votre date. La possibilité d’une intervention doit être confirmée.'),('Quel est le tarif du massage à domicile à Sousse ?','Le tarif, la durée et d’éventuels frais de trajet sont à confirmer directement avec La Vita Spa.')]
  },
  'ar':{
   'name':'سوسة','lead':'تحب مساج استرخاء في دارك في سوسة أو سهلول؟ ابعث الحي والنهار باش نتأكدوا من إمكانية التنقل.',
   'h1':'مساج في الدار <em>بسوسة.</em>',
   'h2':'مساج في الدار بسوسة على الطلب',
   'intro':'المركز متاع La Vita Spa موجود في شارع باكستان سهلول. كان تحب جلسة مساج في دارك، تنجم تبعث المنطقة متاعك، والفريق يأكدلك إذا التنقل متوفر في الوقت المطلوب.',
   'h3':'في سهلول، خزامة، حمام سوسة أو غيرهم؟',
   'zones':'اذكر الحي متاعك: سهلول، خزامة، حمّام سوسة، وسط المدينة أو أي مكان آخر. هاذم أمثلة للاستفسار موش وعد بالتنقل لجميع المناطق. التوفر يتأكد مع الفريق.',
   'h4':'كيفاش تجهّز للموعد؟',
   'prep':'حضّر بلاصة هادئة، واسأل على المدّة، اللوازم، السعر الجملي ومصاريف التنقل المحتملة. ابعث التاريخ والساعة اللي يناسبوك واستنّى تأكيد الفريق.',
   'extra':'تنجم زادة تجي <a href="/ar/massage-sousse/">للمركز في سهلول</a> للمساج والحمّام الفردي والعناية بالوجه على موعد.',
   'q':[('تنجموا تجيو لسهلول أو حمام سوسة؟','ابعثلنا الحي والتاريخ، والفريق يثبّت توفر التنقل.'),('قداش يكلف المساج في الدار؟','السعر والمدة ومصاريف التنقل تتحدد قبل تأكيد الموعد.')]
  }
 },
 'tunis':{
  'fr':{
   'name':'Tunis','lead':'Massage à domicile à Tunis : demandez la disponibilité et les conditions d’un éventuel déplacement depuis Sousse.',
   'h1':'Massage à domicile <em>Tunis.</em>',
   'h2':'Tunis : une demande de déplacement à étudier',
   'intro':'La Vita Spa est un espace de bien-être basé à Sahloul, Sousse. Il ne dispose pas d’un centre physique à Tunis. Pour une demande de massage à domicile dans la capitale, l’équipe peut examiner votre adresse et votre date avant de confirmer toute possibilité de déplacement.',
   'h3':'Tunis centre, La Marsa, Les Berges du Lac : précisez l’adresse',
   'zones':'Que vous soyez à El Menzah, La Marsa, aux Berges du Lac ou dans un autre quartier, précisez votre secteur exact. Ces noms servent uniquement d’exemples pour les demandes, sans représenter des antennes du spa ou une couverture permanente.',
   'h4':'Anticiper le trajet et les modalités',
   'prep':'Un déplacement de Sousse à Tunis nécessite une organisation particulière. Demandez si la visite est possible, combien de temps elle durerait, si des frais de trajet s’appliquent et à quel moment le rendez-vous devient confirmé. Une date souhaitée ne constitue pas un engagement.',
   'extra':'Si vous visitez Sousse, vous pouvez également demander un <a href="/massage-sousse/">rendez-vous massage dans nos locaux à Sahloul</a>.',
   'q':[('La Vita Spa possède-t-il une adresse à Tunis ?','Non, l’établissement est Rue Pakistan, Sahloul, Sousse.'),('Peut-on demander une séance à La Marsa ou au Lac ?','Vous pouvez faire la demande en précisant la zone. Le déplacement est soumis à confirmation.')]
  },
  'ar':{
   'name':'تونس','lead':'مساج في الدار بتونس العاصمة: ابعث المنطقة والموعد باش نتأكدوا من إمكانية التنقل من سوسة.',
   'h1':'مساج في الدار <em>بتونس.</em>',
   'h2':'تونس العاصمة: نثبتوا إمكانية التنقل قبل الموعد',
   'intro':'مقرّ La Vita Spa في سهلول سوسة، موش في تونس العاصمة. كان تحب تسأل على جلسة مساج في الدار في تونس، ابعث الحي والتاريخ باش الفريق ينجم يثبت إذا التنقل ممكن.',
   'h3':'المرسى، البحيرة، المنزه ولا وسط تونس؟',
   'zones':'اذكر الحي بالضبط، سواء البحيرة، المرسى، المنزه، وسط العاصمة أو غيرهم. هاذي مناطق للاستفسار فقط، موش فروع ولا تغطية مضمونة.',
   'h4':'التنقل من سوسة يحتاج ترتيب',
   'prep':'اسأل على إمكانية الزيارة، المدّة، السعر ومصاريف الطريق إن وجدت. ما تعتبرش الطلب تأكيد حجز قبل ردّ الفريق.',
   'extra':'تنجم زادة تزور <a href="/ar/massage-sousse/">المركز في سهلول سوسة</a> على موعد.',
   'q':[('عندكم فرع في تونس؟','لا، المركز في سهلول سوسة.'),('تنجموا تجيو للمرسى أو البحيرة؟','ابعثلنا الحي والتاريخ، ونتثبتولك من إمكانية التنقل.')]
  }
 },
 'nabeul':{
  'fr':{
   'name':'Nabeul','lead':'De Nabeul à Hammamet, renseignez-vous sur une éventuelle séance de massage bien-être chez vous.',
   'h1':'Massage à domicile <em>Nabeul.</em>',
   'h2':'Nabeul et Hammamet : votre demande en quelques informations',
   'intro':'La Vita Spa est situé à Sahloul, Sousse. Pour une demande de massage à domicile à Nabeul ou Hammamet, l’équipe doit d’abord vérifier le déplacement possible vers votre adresse, la date souhaitée et le tarif final.',
   'h3':'Nabeul, Hammamet, Dar Chaabane : votre localisation compte',
   'zones':'Précisez Nabeul ville, Hammamet, Yasmine Hammamet, Dar Chaabane ou une autre localité du gouvernorat. Ces secteurs sont cités pour orienter les demandes et non pour annoncer des équipes présentes sur place en permanence.',
   'h4':'Un séjour dans un hébergement ? Vérifiez les accès',
   'prep':'Pour une séance dans un logement de vacances ou un hôtel, renseignez-vous sur les conditions d’accès du lieu. Demandez toujours la durée, le matériel à prévoir, la disponibilité, les frais de déplacement et le prix total avant de confirmer.',
   'extra':'Pour une séance au spa, l’adresse reste <a href="/massage-sousse/">Rue Pakistan, Sahloul, Sousse</a>. Aucun autre salon La Vita Spa n’est indiqué sur ce site.',
   'q':[('Peut-on demander un massage à Hammamet ?','Oui, une demande est possible. L’intervention dépend de la date et de la confirmation du spa.'),('Intervenez-vous dans un hôtel à Nabeul ?','Cela dépend de l’autorisation du lieu et de la disponibilité du professionnel.')]
  },
  'ar':{
   'name':'نابل','lead':'في نابل أو الحمامات؟ ابعث المنطقة والتاريخ باش نتأكدوا من إمكانية جلسة مساج في الدار.',
   'h1':'مساج في الدار <em>بنابل.</em>',
   'h2':'نابل والحمامات: جلسة استرخاء على الطلب',
   'intro':'La Vita Spa مركز موجود في سهلول سوسة. كان تحب مساج في دارك بنابل أو الحمامات، لازمنا نثبتوا إمكانية التنقل حسب المكان والتاريخ قبل تأكيد الموعد.',
   'h3':'نابل، الحمامات، دار شعبان: حدّد المنطقة',
   'zones':'قلنا كانك في نابل المدينة، الحمامات، ياسمين الحمامات، دار شعبان ولا بلاصة أخرى. المناطق المذكورة للطلبات فقط، موش فروع للمركز ولا تغطية دائمة.',
   'h4':'إذا أنت في إقامة أو أوتيل',
   'prep':'تأكد من قوانين مكان الإقامة، واسأل على التجهيزات والمدة والكلفة الجملية ومصاريف التنقل الممكنة قبل التأكيد.',
   'extra':'عنوان المركز الثابت: <a href="/ar/massage-sousse/">شارع باكستان سهلول سوسة</a>.',
   'q':[('تنجموا تجيو للحمامات؟','ابعثلنا التاريخ والعنوان باش نتثبتولك من التوفر.'),('تنجم الجلسة تكون في أوتيل؟','حسب موافقة الإقامة وإمكانية تنقل المختص.')]
  }
 }
}

def register(g):
    pages=g['PAGES'];nav=g['NAV']
    for key,translations in CITY.items():
        for lang,d in translations.items():
            pref='/ar/' if lang=='ar' else '/'
            alt='/'+('' if lang=='ar' else 'ar/')+'massage-a-domicile-'+key+'/'
            p=pref+'massage-a-domicile-'+key+'/'
            head=('مساج في الدار '+d['name'] if lang=='ar' else 'Massage à domicile '+d['name'])
            pages[p]={('fr' if lang=='ar' else 'ar'):alt,
                      'title':head+' | La Vita Spa Sousse',
                      'desc':('طلب مساج منزلي في '+d['name']+' حسب إمكانية التنقل والموعد؛ اتصل بـLa Vita Spa لتأكيد السعر.' if lang=='ar' else 'Massage bien-être à domicile '+d['name']+' sur demande. Vérifiez la disponibilité, les frais de déplacement et les créneaux auprès de La Vita Spa.')}
    pages['/massage-a-domicile/']={'ar':'/ar/massage-a-domicile/',
        'title':'Massage à domicile Sousse, Tunis & Nabeul | La Vita Spa',
        'desc':'Massage bien-être à domicile sur demande à Sousse, Tunis et Nabeul. Indiquez quartier et date pour vérifier déplacements, prix et disponibilités.'}
    pages['/ar/massage-a-domicile/']={'fr':'/massage-a-domicile/',
        'title':'مساج في الدار سوسة وتونس ونابل | La Vita Spa',
        'desc':'اطلب مساج استرخاء في دارك بسوسة أو تونس أو نابل. ابعث الحي والنهار المفضّل للتثبّت من إمكانية التنقل والسعر.'}
    nav['fr']=[('Accueil','/'),('Soins','/soins/'),('À domicile','/massage-a-domicile/'),('Massage Sousse','/massage-sousse/'),('Hammam','/hammam-sousse/'),('Contact','/contact/')]
    nav['ar']=[('الرئيسية','/ar/'),('خدماتنا','/ar/soins/'),('مساج في الدار','/ar/massage-a-domicile/'),('مساج سوسة','/ar/massage-sousse/'),('حمّام','/ar/hammam-sousse/'),('اتصل بنا','/ar/contact/')]
    g['domicile_teaser']=lambda loc:teaser(g,loc)
    g['domicile_mini']=lambda loc:mini(loc)


def city_cards(loc,exclude=None):
    pre='/ar/' if loc=='ar' else '/';ar=loc=='ar'
    return '<div class="dom-city-grid">'+''.join(
        f'<a class="dom-city-card" href="{pre}massage-a-domicile-{key}/">'
        f'<span class="dom-city-number">0{i+1}</span><span class="dom-city-label">{"مساج في الدار" if ar else "MASSAGE À DOMICILE"}</span>'
        f'<strong>{CITY[key][loc]["name"]}</strong><span class="dom-city-foot">{"التفاصيل" if ar else "Découvrir les détails"} <span>↗</span></span></a>'
        for i,key in enumerate(CITY) if key!=exclude)+'</div>'


def teaser(g,loc):
    ar=loc=='ar';pre='/ar/' if ar else '/';eyebrow=g['eyebrow']
    return f'''<section class="dom-teaser section-pad-sm" aria-labelledby="dom-teaser-heading"><div class="container"><div class="dom-teaser-top"><div>{eyebrow('LA VITA SPA · '+('حتى لدارك' if ar else 'CHEZ VOUS'),'rose')}<h2 id="dom-teaser-heading" class="section-title">{'مساج <em>في دارك.</em>' if ar else 'Le bien-être, <em>chez vous.</em>'}</h2><p class="section-lead">{'سوسة، تونس ونابل: ابعث منطقتك وموعدك، والتنقل والسعر يتأكدوا حسب التوفر.' if ar else 'À Sousse, Tunis ou Nabeul, partagez votre quartier et votre date : chaque demande de déplacement est vérifiée individuellement.'}</p></div><a class="btn btn-dark" href="{pre}massage-a-domicile/">{'اكتشف الخدمة' if ar else 'Découvrir le massage à domicile'} ↗</a></div>{city_cards(loc)}<p class="dom-disclaimer">{'مقرّ La Vita Spa في سهلول سوسة. التنقل للمدن الأخرى موش مضمون ويستلزم تأكيد.' if ar else 'Le spa reste basé à Sahloul, Sousse. Toute intervention à domicile exige une confirmation préalable.'}</p></div></section>'''


def mini(loc):
    ar=loc=='ar';pre='/ar/' if ar else '/'
    return f'''<section class="dom-mini"><div class="container dom-mini-flex"><div><h2>{'تحب مساج في الدار؟' if ar else 'Envie d’un massage à domicile ?'}</h2><p>{'اطلب معلومات على التنقل لسوسة، تونس ونابل.' if ar else 'Renseignez-vous sur les demandes à Sousse, Tunis et Nabeul.'}</p></div><a class="btn btn-outline-dark" href="{pre}massage-a-domicile/">{'شوف التفاصيل' if ar else 'En savoir plus'} ↗</a></div></section>'''


def faq(g,items,loc):
    return g['faq_render'](items,loc=='ar')


def generate(g):
    for loc in ('fr','ar'):
        hub(g,loc)
        for key in CITY:city_page(g,key,loc)


def hub(g,loc):
    ar=loc=='ar';pre='/ar/' if ar else '/';path=pre+'massage-a-domicile/'
    hero=g['inner_hero'](loc,path,'مساج <em>في الدار.</em>' if ar else 'Massage <em>à domicile.</em>',
        'سوسة، تونس ونابل: ابعثلنا الحي والموعد اللي تحب عليه باش نتثبتوا معاك من التوفر والتكلفة.' if ar else 'Chez vous, selon votre ville : prenez contact avec La Vita Spa pour vérifier la possibilité d’un massage bien-être à domicile.',
        ['Sousse','Tunis','Nabeul'] if not ar else ['سوسة','تونس','نابل'])
    content=f'''<section class="section-pad-sm dom-hub"><div class="container dom-hub-layout"><div>{g['eyebrow']('LA VITA SPA · '+('على الطلب' if ar else 'VOTRE MOMENT'),'rose')}<h2 class="section-title">{'راحتك <em>في دارك.</em>' if ar else 'Un moment pour vous, <em>sans sortir.</em>'}</h2><p class="section-lead">{'إعطينا المدينة والحي والتاريخ، ونثبتوا معاك من إمكانية التنقل. ما فما حتى حجز آلي بلا تأكيد من الفريق.' if ar else 'Choisissez votre ville, précisez votre quartier et votre date préférée, puis recevez une réponse de l’équipe sur la faisabilité, les modalités et le tarif.'}</p><div class="dom-steps"><div><b>01</b><span>{'اختار المدينة والحي' if ar else 'Votre ville et votre quartier'}</span></div><div><b>02</b><span>{'حدد موعد تحب عليه' if ar else 'Votre date souhaitée'}</span></div><div><b>03</b><span>{'تأكيد التنقل والسعر' if ar else 'Confirmation et prix avant la séance'}</span></div></div>{g['booking']('نطلب مساج في الدار' if ar else 'Demander un massage','Domicile')}</div><div class="dom-hub-image"><img src="/assets/img/massage-bien-etre.webp" width="690" height="830" loading="lazy" alt="{'أجواء المساج من La Vita Spa' if ar else 'Ambiance massage et soin La Vita Spa'}"><span class="dom-image-caption">LA VITA SPA · BIEN-ÊTRE</span></div></div></section>'''
    cities=f'''<section class="section-pad-sm dom-zones"><div class="container">{g['eyebrow']('02 / '+('الولايات' if ar else 'NOS VILLES'),'rose')}<h2 class="section-title">{'اختار <em>مدينتك.</em>' if ar else 'Choisissez <em>votre ville.</em>'}</h2><p class="section-lead">{'كل مدينة عندها تفاصيلها؛ تأكد من إمكانية التنقل قبل حجز الموعد.' if ar else 'Consultez les informations pratiques de chaque zone avant de demander un déplacement.'}</p>{city_cards(loc)}<p class="dom-disclaimer">{'المقرّ الثابت الوحيد في سهلول سوسة؛ ما فماش فروع معلنة في تونس ولا نابل.' if ar else 'Le seul local La Vita Spa indiqué est à Sahloul, Sousse. Les autres villes ne sont pas des succursales.'}</p></div></section>'''
    qs=[('Le formulaire confirme-t-il un rendez-vous ?','Non. Il ouvre WhatsApp avec votre demande. Vous attendez la réponse du spa pour confirmer.'),('Les frais de trajet sont-ils compris ?','Demandez au spa le coût total et les éventuels frais de déplacement avant de valider.'),('Le hammam se déplace-t-il aussi ?','Le hammam individuel est présenté dans les locaux de Sahloul. Le service à domicile mentionné ici concerne une demande de massage.') ] if not ar else [('الطلب على واتساب يثبت الحجز؟','لا، التثبيت يكون بعد ما يردّ عليك الفريق.'),('مصاريف التنقل داخلة في السعر؟','اسأل على الكلفة الجملية قبل التأكيد.'),('الحمام الفردي زادة في الدار؟','الحمام الفردي معلن في مقرّ سهلول، والخدمة المنزلية هنا تخصّ طلب المساج.')]
    footer=f'<section class="section-pad-sm"><div class="container dom-faqwrap">{faq(g,qs,loc)}</div></section>'
    schema=[{'@context':'https://schema.org','@type':'Service','name':'Massage bien-être à domicile sur demande','serviceType':'Massage bien-être à domicile','provider':{'@id':g['uri']('/#spa')},'areaServed':[{'@type':'City','name':name} for name in ('Sousse','Tunis','Nabeul')]},g['jsonld_faq'](qs)]
    g['page'](path,hero+content+cities+footer+g['big_cta'](loc),schema)


def city_page(g,key,loc):
    d=CITY[key][loc];ar=loc=='ar';pre='/ar/' if ar else '/';p=pre+'massage-a-domicile-'+key+'/'
    city={'sousse':'Sousse','tunis':'Tunis','nabeul':'Nabeul'}[key]
    hero=g['inner_hero'](loc,p,d['h1'],d['lead'],[city, 'حسب التوفر' if ar else 'Déplacement sur demande'])
    body=f'''<section class="section-pad-sm"><div class="container content-grid"><article class="prose dom-article"><h2>{d['h2']}</h2><p>{d['intro']}</p><h2>{d['h3']}</h2><p>{d['zones']}</p><h2>{d['h4']}</h2><p>{d['prep']}</p><div class="dom-info"><strong>{'معلومة مهمّة' if ar else 'À savoir avant de confirmer'}</strong><p>{'الجلسة للراحة موش علاج طبي، والموعد والتكلفة والتنقل يتأكدوا قبل أي جلسة.' if ar else 'La prestation de bien-être ne remplace pas un traitement médical. Le rendez-vous et le coût total nécessitent une validation du spa.'}</p></div><p>{d['extra']}</p>{faq(g,d['q'],loc)}</article><aside class="aside-box dom-aside">{g['eyebrow']('LA VITA · '+city.upper(),'rose')}<h3>{'ابعث طلبك' if ar else 'Demandez votre créneau.'}</h3><p>{'قلنا المنطقة والنهار باش نتثبتوا من إمكانية التنقل.' if ar else 'Indiquez quartier et date : votre demande sera transmise à l’équipe pour vérification.'}</p>{g['booking']('مساج في الدار' if ar else 'Demander à domicile','Domicile:'+city)}<dl class="aside-details"><div><dt>{'المدينة' if ar else 'Votre ville'}</dt><dd>{d['name']}</dd></div><div><dt>{'مقرّ المركز' if ar else 'Adresse du spa'}</dt><dd>{'سهلول، سوسة' if ar else 'Rue Pakistan, Sahloul, Sousse'}</dd></div><div><dt>{'الهاتف' if ar else 'Téléphone'}</dt><dd><a href="tel:+21625213968" dir="ltr">+216 25 213 968</a></dd></div></dl></aside></div></section>'''
    similar=f'''<section class="section-pad-sm dom-other"><div class="container">{g['eyebrow']('LA VITA SPA · '+('المدن الأخرى' if ar else 'AUTRES VILLES'),'rose')}<h2 class="section-title">{'تلوّج على <em>مدينة أخرى؟</em>' if ar else 'Et dans une <em>autre ville ?</em>'}</h2>{city_cards(loc,key)}<a class="text-link" href="{pre}massage-a-domicile/">{'جميع التفاصيل' if ar else 'Tous les renseignements'} ↗</a></div></section>'''
    schema=[{'@context':'https://schema.org','@type':'Service','serviceType':'Massage bien-être à domicile sur demande',
             'name':('مساج في الدار '+d['name']) if ar else ('Massage à domicile '+city),
             'provider':{'@id':g['uri']('/#spa')},'areaServed':{'@type':'City','name':city},
             'description':g['PAGES'][p]['desc']},g['jsonld_faq'](d['q'])]
    g['page'](p,hero+body+similar+g['big_cta'](loc),schema)
