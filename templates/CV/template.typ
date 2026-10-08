#let raw_data = sys.inputs.at("data", default: "{}")
#let data = json.decode(raw_data)

#set page(
  paper: "us-letter",
  margin: (x: 1.2cm, y: 1.2cm)
)

#set text(
  font: "Arial",
  size: 9.5pt,
  fill: rgb("#000000")
)

#set par(justify: false, leading: 0.55em)

// CABECERA
#align(center)[
  #text(size: 15pt, weight: "bold")[#data.at("user_name", default: "")] \
  #v(2pt)
  #text(size: 9pt)[
    #data.at("user_location", default: "") | #data.at("user_number", default: "") | #data.at("user_email", default: "") | #data.at("user_linkedin", default: "")
  ]
]

#v(6pt)

// FUNCIÓN DE SECCIONES
#let section(title) = {
  v(6pt)
  text(weight: "bold", size: 10pt)[#upper(title)]
  v(-4pt)
  line(length: 100%, stroke: 0.7pt + black)
  v(2pt)
}

// EXPERIENCIA
#section("Experience")
#for exp in data.at("experiences", default: ()) {
  grid(
    columns: (1fr, auto),
    align: (left, right),
    [*#exp.at("company_name", default: "")*], [#exp.at("start_date", default: "") – #exp.at("end_date", default: "")],
    [_#exp.at("role", default: "")_], [#exp.at("location", default: "")]
  )
  v(-2pt)
  let bullets = exp.at("description", default: ())
  for item in bullets {
    list.item([#item])
  }
  v(2pt)
}

// SKILLS
#section("Skills")
*Languages:* #data.at("languages_list", default: "") \
*Backend & Frameworks:* #data.at("back_and_frm_list", default: "") \
*Cloud & Systems:* #data.at("cloud_and_system_list", default: "") \
*Data & Tooling:* #data.at("data_and_tooling", default: "")

// EDUCACIÓN
#section("Education")
#for edu in data.at("education_list", default: ()) {
  grid(
    columns: (1fr, auto),
    align: (left, right),
    [*#edu.at("institution", default: "")*], [#edu.at("dates", default: "")],
    [_#edu.at("degree", default: "")_], [#edu.at("location", default: "")]
  )
}