# 0001. Design: navy technical analyst

- Status: accepted
- Date: 2026-10-31

## Goal

In five seconds, a hiring manager should read: this analyst ships real
systems. The message comes from the October 2026 cover letter for the YVR
Senior Technical Analyst role: someone who uses technical depth to understand
how systems interact and turns that into practical solutions.

Audience: hiring managers and recruiters for analyst, analytics and technical
analyst roles. Developers reading the source are secondary.

## Page hierarchy

The order is claim, evidence, depth, breadth, action. Do not reorder without a
reason.

1. Hero: the claim, "I turn business problems into working systems."
2. Proof strip: four numbers overlapping the hero, so the eye falls straight
   from claim to evidence.
3. Featured case study: Maxio. It is the strongest proof, so it gets the most
   space. The system diagram shows how systems interact, which is the message
   itself. The five steps match the letter's full cycle.
4. Now building: one line showing current direction.
5. Side projects: each card leads with the skill it `proves`, not the tech.
6. Skills: scannable groups for keyword readers.
7. Closing call to action.

## Colour

Navy is the brand, not an accent. All tokens are on `:root` in
`static/style.css`.

| Role | Light | Dark |
|---|---|---|
| Brand surface (hero, featured card, contact) | `#0a1f44` | `#0a1f44` |
| Page background | `#f5f7fb` | `#071530` |
| Card | `#ffffff` | `#0f2348` |
| Text | `#0a1f44` | `#eaf0fa` |
| Muted text | `#4a5a75` | `#a9b8d0` |
| Text accent | `#1d4ed8` | `#93c5fd` |
| Diagram lines, focus ring | `#3b82f6` | `#3b82f6` |

`#3b82f6` is about 3.7:1 on white, which fails WCAG AA for body text, so it is
used only for lines and focus rings. Text accents use `#1d4ed8` on light
surfaces. The hero stays navy in both colour schemes so the brand never
inverts.

## Type and layout

- System sans stack, with Inter if the visitor has it. No web font: ADR 0001
  keeps the site free of external requests and JavaScript.
- Strong size contrast: fluid hero headline up to 4.25rem at weight 800 with
  tight tracking; small uppercase labels; tabular numerals for stats.
- Content width 1120px, 8px spacing scale, 96px between sections on desktop.
- Breakpoints: 900px stacks the hero and makes the portrait a small circle;
  640px gives a single column and a vertical system diagram.
- The system diagram is HTML, not SVG, so its text stays readable on phones.
- Motion is limited to small hover feedback and honours
  `prefers-reduced-motion`.

## Content rules

- Publish only facts from the cover letter or from public repos.
- The letter names REST and JSON-RPC without saying which integration uses
  which, so the diagram must not label individual links with a protocol.
- Do not publish: phone, email, ARR or CAD figures, target employers, the
  Azure and years-of-experience caveats from the letter, or anything still open
  in `render-cv/TODO.md`.
- Project copy states what the project proves before what it uses.

## Portrait

`static/portrait.jpg` is the LinkedIn profile photo, cropped square to 468px.
Its warm background contrasts with the navy, which helps it stand out in the
hero. A sharper photo can replace the file at the same path and size.

## Rejected options

- Uniform project card list: gives the page no focal point and buries the
  strongest work.
- Leading with side projects: reads as a hobbyist developer, not an analyst.
- Conway's Game of Life entry: a fun project, but it dilutes the positioning.
- Google Fonts and client-side JavaScript: not worth an exception to ADR 0001.

## Extending the page

- New project: add a `[[projects]]` table with a `proves` line. Only one
  project should be `featured`.
- New case study: keep one on the page and rotate it. Two compete for the focal
  point.
- New colour: add a token on `:root` and a dark value, and check AA contrast.
