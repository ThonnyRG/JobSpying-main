#let raw_data = sys.inputs.at("data", default: "{}")
#let data = json(bytes(raw_data))

#set page(
  paper: "us-letter",
  margin: (x: 2cm, top: 2cm, bottom: 2.5cm)
)

#set text(
  font: "Arial",
  size: 10pt,
  fill: rgb("#333333")
)

#set par(justify: true, leading: 0.65em)

// CABECERA / DESTINATARIO Y REMITENTE
#grid(
  columns: (1fr, 1fr),
  align: (left, right),
  [
    #text(size: 11pt, weight: "bold", fill: rgb("#000000"))[To:] \
    #v(2pt)
    #text(size: 11pt, weight: "bold")[#data.at("company_name", default: "Company Name")] \
    #text(size: 10pt)[Human Resources Manager]
  ],
  [
    #text(size: 13pt, weight: "bold", fill: rgb("#000000"))[Jesús Antonio Morales Cruz] \
    #v(1pt)
    #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Software Engineer & Data Engineer]
  ]
)

#v(20pt)

// PÁRRAFOS DEL CUERPO
#let paragraphs = data.at("paragraphs", default: ())
#for p in paragraphs [
  #p
  #v(8pt)
]

#v(12pt)

// CIERRE Y FIRMA
#text()[Thank you for your consideration.]

#v(12pt)

#text()[Sincerely,] \
#v(4pt)
#text(weight: "bold", size: 11pt)[Jesús Antonio Morales Cruz]

#v(1fr)

// PIE DE PÁGINA / CONTACTO CON IMÁGENES DEtemplates/src/
#line(length: 100%, stroke: 0.5pt + rgb("#cccccc"))
#v(6pt)

#align(center)[
  #grid(
    columns: (auto, auto, auto, auto),
    column-gutter: 16pt,
    align: center + horizon,
    
    // Icono LinkedIn
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("templates\src\image1.png", height: 10pt),
        text(size: 8.5pt)[linkedin.com/in/jamc17]
      )
    ],
    // Icono GitHub
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("templates\src\image2.png", height: 10pt),
        text(size: 8.5pt)[@ThonnyRG]
      )
    ],
    // Icono Email
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image3.png", height: 10pt),
        text(size: 8.5pt)[jesus2013.jamc7\@gmail.com]
      )
    ],
    // Icono Teléfono
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image4.png", height: 10pt),
        text(size: 8.5pt)[+52 921 103 1160]
      )
    ]
  )
]#let raw_data = sys.inputs.at("data", default: "{}")
#let data = json(bytes(raw_data))

#set page(
  paper: "us-letter",
  margin: (x: 2cm, top: 2cm, bottom: 2.5cm)
)

#set text(
  font: "Arial",
  size: 10pt,
  fill: rgb("#333333")
)

#set par(justify: true, leading: 0.65em)

// CABECERA / DESTINATARIO Y REMITENTE
#grid(
  columns: (1fr, 1fr),
  align: (left, right),
  [
    #text(size: 11pt, weight: "bold", fill: rgb("#000000"))[To:] \
    #v(2pt)
    #text(size: 11pt, weight: "bold")[#data.at("company_name", default: "Company Name")] \
    #text(size: 10pt)[Human Resources Manager]
  ],
  [
    #text(size: 13pt, weight: "bold", fill: rgb("#000000"))[Jesús Antonio Morales Cruz] \
    #v(1pt)
    #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Software Engineer & Data Engineer]
  ]
)

#v(20pt)

// PÁRRAFOS DEL CUERPO
#let paragraphs = data.at("paragraphs", default: ())
#for p in paragraphs [
  #p
  #v(8pt)
]

#v(12pt)

// CIERRE Y FIRMA
#text()[Thank you for your consideration.]

#v(12pt)

#text()[Sincerely,] \
#v(4pt)
#text(weight: "bold", size: 11pt)[Jesús Antonio Morales Cruz]

#v(1fr)

// PIE DE PÁGINA / CONTACTO CON IMÁGENES DEtemplates/src/
#line(length: 100%, stroke: 0.5pt + rgb("#cccccc"))
#v(6pt)

#align(center)[
  #grid(
    columns: (auto, auto, auto, auto),
    column-gutter: 16pt,
    align: center + horizon,
    
    // Icono LinkedIn
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image1.png", height: 10pt),
        text(size: 8.5pt)[linkedin.com/in/jamc17]
      )
    ],
    // Icono GitHub
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image2.png", height: 10pt),
        text(size: 8.5pt)[@ThonnyRG]
      )
    ],
    // Icono Email
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image3.png", height: 10pt),
        text(size: 8.5pt)[jesus2013.jamc7\@gmail.com]
      )
    ],
    // Icono Teléfono
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image4.png", height: 10pt),
        text(size: 8.5pt)[+52 921 103 1160]
      )
    ]
  )
]#let raw_data = sys.inputs.at("data", default: "{}")
#let data = json(bytes(raw_data))

#set page(
  paper: "us-letter",
  margin: (x: 2cm, top: 2cm, bottom: 2.5cm)
)

#set text(
  font: "Arial",
  size: 10pt,
  fill: rgb("#333333")
)

#set par(justify: true, leading: 0.65em)

// CABECERA / DESTINATARIO Y REMITENTE
#grid(
  columns: (1fr, 1fr),
  align: (left, right),
  [
    #text(size: 11pt, weight: "bold", fill: rgb("#000000"))[To:] \
    #v(2pt)
    #text(size: 11pt, weight: "bold")[#data.at("company_name", default: "Company Name")] \
    #text(size: 10pt)[Human Resources Manager]
  ],
  [
    #text(size: 13pt, weight: "bold", fill: rgb("#000000"))[Jesús Antonio Morales Cruz] \
    #v(1pt)
    #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Software Engineer & Data Engineer]
  ]
)

#v(20pt)

// PÁRRAFOS DEL CUERPO
#let paragraphs = data.at("paragraphs", default: ())
#for p in paragraphs [
  #p
  #v(8pt)
]

#v(12pt)

// CIERRE Y FIRMA
#text()[Thank you for your consideration.]

#v(12pt)

#text()[Sincerely,] \
#v(4pt)
#text(weight: "bold", size: 11pt)[Jesús Antonio Morales Cruz]

#v(1fr)

// PIE DE PÁGINA / CONTACTO CON IMÁGENES DEtemplates/src/
#line(length: 100%, stroke: 0.5pt + rgb("#cccccc"))
#v(6pt)

#align(center)[
  #grid(
    columns: (auto, auto, auto, auto),
    column-gutter: 16pt,
    align: center + horizon,
    
    // Icono LinkedIn
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image1.png", height: 10pt),
        text(size: 8.5pt)[linkedin.com/in/jamc17]
      )
    ],
    // Icono GitHub
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image2.png", height: 10pt),
        text(size: 8.5pt)[@ThonnyRG]
      )
    ],
    // Icono Email
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image3.png", height: 10pt),
        text(size: 8.5pt)[jesus2013.jamc7\@gmail.com]
      )
    ],
    // Icono Teléfono
    [
      #grid(
        columns: (auto, auto),
        gutter: 4pt,
        align: horizon,
        image("/templates/src/image4.png", height: 10pt),
        text(size: 8.5pt)[+52 921 103 1160]
      )
    ]
  )
]