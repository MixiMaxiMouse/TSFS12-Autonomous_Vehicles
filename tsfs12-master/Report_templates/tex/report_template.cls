% ==============================================================================
%  report_template.cls - v0.1
%  2025-07-17 Erik Frisk
%  Small template for reports
\ProvidesClass{report_template}[2025/07/17 report_template Class v. 0.1]
\NeedsTeXFormat{LaTeX2e}

\RequirePackage[utf8]{inputenc} % Required for inputting international characters
\RequirePackage[T1]{fontenc} % Output font encoding for international characters

\def\@@ptsize{10pt}
\DeclareOption{10pt}{\def\@@ptsize{10pt}}
\DeclareOption{11pt}{\def\@@ptsize{11pt}}
\DeclareOption{12pt}{\def\@@ptsize{12pt}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClassWithOptions{article}
\RequirePackage{babel}
\RequirePackage{xkeyval}
\RequirePackage{setspace}
\RequirePackage{fancyhdr}
\RequirePackage{geometry}
\RequirePackage{titlesec}
\RequirePackage[lf]{carlito}
\RequirePackage{iflang}

\RequirePackage[backend=biber, style=numeric-comp, maxnames=99]{biblatex}

\renewcommand*\oldstylenums[1]{\carlitoOsF #1}

\geometry{a4paper, margin=1in, top=1in}
\linespread{1.0}
\setlength{\headheight}{15pt}

\titleformat*{\section}{\Large\sffamily}
\titleformat*{\subsection}{\large\sffamily}
\titleformat*{\subsubsection}{\sffamily}

\def\emailstring{E-mail}
\IfLanguageName{swedish}{\def\emailstring{E-post}}{}


\newtoks\authorlist@toks
\newcommand{\authorlist}{
    \the\authorlist@toks
}

\define@key{authorlist}{email}{\def\AuthorEmail{#1}}
\define@key{authorlist}{liuid}{\def\AuthorLiUID{#1}}

\ExecuteOptionsX<authorlist>{%
	email="",
	liuid=""
}

\renewcommand*\author[2][]{%
	\authorlist@toks=\expandafter{\the\authorlist@toks{
	\begingroup
	\setkeys{authorlist}{#1}
	\noindent\uppercase{#2}\\
	\if\AuthorEmail\relax
	\else
		\noindent\hspace*{7mm}\emailstring: \AuthorEmail\\
	\fi
	\if\AuthorLiUID\relax
	\else
		\noindent\hspace*{7mm}LiU-ID: \AuthorLiUID\\
	\fi
	\par\vspace{0.75em}
	\endgroup}}
}

\renewcommand{\maketitle}{
    \pagestyle{fancy}
    \renewcommand{\headrulewidth}{0pt}
    \fancyfoot[R]{\textit{\@date}}
    \fancyfoot[C]{}
    {
        \raggedleft
        \hspace{0.1\textwidth}
        \rule{1pt}{1.0\textheight}
        \hspace{0.05\textwidth}
        \parbox[b][\textheight]{0.75\textwidth}{\raggedright
            \vspace{0.1\textheight}
            \begin{spacing}{1.0}
                \Huge\linespread{1.5}{\textsf{\@title}}
            \end{spacing}
            \vfill
            \authorlist
            \vspace{0.05\textheight}
        }
    }
    \clearpage
    \fancyfoot[R]{}
    \fancyhead[L]{}
    \fancyhead[R]{\thepage}
    \renewcommand{\headrulewidth}{0.5pt}
    \setcounter{page}{1}
}

\setlength\bibitemsep{1.25\itemsep}
\setlength\biblabelsep{3mm}
