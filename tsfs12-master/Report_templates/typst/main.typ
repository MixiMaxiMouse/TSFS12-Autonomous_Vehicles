#import "report_template.typ": *
#import "@preview/subpar:0.2.2" // package for subfigures

#show: report.with(
  title: [TSFS12 Hand-in 1:\
    Discrete Path Planning in a Structured Road Network],
  authors: (
    (name: "Firstname Lastname", liuid: "firla002", email: "first.last@student.liu.se"),
    (name: "Firstname Lastname", liuid: "firla002", email: "first.last@student.liu.se"),
  ),
  size: 10pt,
  // date: "2025-01-01",
  // lang: "sv",
)
= Introduction <intro>

Some references: @intro @intro_sub, @eq_abc, @blue_marble, @euclid_algorithm, @tab_table and citations @lavalle2006planning @dubins1957curves @karaman2011sampling @limebeer2015faster @paden2016survey @rawlings2020model, and @oh2015survey.

Equations can be included
$
  f(t + h) = f(t) + f'(t) space.thin h + 1 / (2!) f''(t) space.thin h^2 + cal(O)(h^3)
$<eq_abc>
and so can images as in @blue_marble. Remember to use scalable vector graphics (SVG) for plots and figures, bitmaps is for photos. Tables can also be included, as in @tab_table.
#figure(
  placement: auto,
  caption: [The famous blue marble photo (https://en.wikipedia.org/wiki/The_Blue_Marble).],
  image(
    "figures/blue_marble.jpg",
    width: 40%,
  ),
)<blue_marble>


#figure(placement: auto, caption: [An example table], table(
  columns: 2,
  align: (center, center),
  stroke: none,
  table.header([*Column One*], [*Column Two*]),
  table.hline(stroke: 0.5pt),
  [One], [Two],
  [Three], [Four],
))<tab_table>

Code can be directly included in the text, just specify the language and the code will be syntax highlighted.
```python
def gcd(a, b):
    "Compute the GCD of a and b using Euclid's algorithm."
    while b:
        a, b = b, a % b
    return a
```

#figure(placement: auto, kind: "algorithm", caption: [Euclid's Algorithm in pseudo code.], box(
  width: 80%,
  pseudocode-list(title: [*Euclid's Algorithm*])[
    + *procedure* Euclid($a$, $b$)#h(1fr) $triangle.r$ The GCD of $a$ and $b$
      + $r <- a "mod" b$
      + *while* $r != 0$ do #h(1fr) $triangle.r$ We have the answer if $r$ is 0
        + $a <- b$
        + $b <- r$
        + $r <- a "mod" b$
      + *return* $b$ #h(1fr) $triangle.r$ The GCD is $b$
  ],
))<euclid_algorithm>

#lorem(150)

== Introduction<intro_sub>

#place(top + center, float: true, scope: "parent", clearance: 2em, subpar.grid(
  columns: (1fr, 1fr),
  [#figure(caption: "", image("figures/blue_marble.jpg", width: 50mm))<fig_first_case>],
  [#figure(caption: "", image("figures/blue_marble.jpg", width: 50mm))<fig_second_case>],

  [#figure(caption: "", image("figures/blue_marble.jpg", width: 50mm))<fig_first_case>],
  [#figure(caption: "", image("figures/blue_marble.jpg", width: 50mm))<fig_second_case>],

  caption: [
    Multiple subfigures in a grid layout using the subpar package.],
  label: <fig_sim>,
))

#lorem(150)

= Introduction
#lorem(150)

= Introduction
#lorem(150)

= Introduction
#lorem(150)

== Introduction
#lorem(150)

= Introduction
#lorem(150)

== Introduction
#lorem(150)

#bibliography("references.bib")
