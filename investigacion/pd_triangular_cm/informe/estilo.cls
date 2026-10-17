\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{estilo}
\LoadClass[10pt]{article}

%\RequirePackage{hyperref}
\RequirePackage{verbatim}
%\RequirePackage{attachfile2} % lo comento porque no se usa para nada y solo hizo causar errores.
\RequirePackage{etoolbox}
\RequirePackage{xparse}
\RequirePackage{pgffor}
\RequirePackage{arrayjobx}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[document]{ragged2e}
\RequirePackage{lipsum}
\RequirePackage{translations}
\RequirePackage{ifthen}
\RequirePackage{xstring}
\RequirePackage[a4paper, left=30mm, right=30mm, top=30mm, bottom=30mm, marginpar=25mm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage{csquotes}
\graphicspath{{images/}} % indico la carpeta raíz las imágenes

\RequirePackage{tikz}

\RequirePackage{xfp}

% Función para poner los asteriscos
\newcommand{\andreas}[5][1.0]{
    \begin{scope}[shift={(#2,#3)},rotate=45,scale=#4,transparency group,opacity=#1]
        \fill[fill=#5] (0,0) -- (0,1) -- (3,1) -- (3,0);
        \fill[fill=#5] (1,-1) -- (2,-1) -- (2,2) -- (1,2);
    \end{scope}
}

\newcommand{\andreasline}{
    \centering\begin{tikzpicture}
        \newcommand\numcross{29}
        \foreach \n in {1,...,\the\numexpr\numcross\relax} {
            \andreas[\fpeval{0.9*sin((\n + 1)*pi/(\numcross+2))}]{0.5*\n}{0}{0.10}{black}
        }
    \end{tikzpicture}
}

\newcommand{\andreaslineslim}{
    \centering\begin{tikzpicture}[baseline]
        \newcommand\numcross{74}
        \foreach \n in {1,...,\the\numexpr\numcross\relax} {
            \andreas[0.75]{0.2*\n}{0}{0.04}{black}
        }
    \end{tikzpicture}
}

%------------------------------------------------------------------------------
%	Función para contar palabras
%------------------------------------------------------------------------------
%\newcommand{\quickwordcount}[1]{%
%  \immediate\write18{texcount -1 -sum=1,1,1,0,0,1,1. -merge -q -nobib #1.tex > #1-words.sum }%
%  \input{#1-words.sum} {palabras}%
%}
%\newcommand{\quickwordcount}[1]{%
%  \immediate\write18{texcount -1 -sum -merge #1.tex > #1-words}%
%  \input{#1-words}words%
%}
\newcommand{\quickwordcount}[1]{%
  \immediate\write18{texcount -total -sum -1 -merge #1.tex > #1-words}%
  \input{#1-words} palabras%
}

%------------------------------------------------------------------------------
%	HEADERS Y FOOTERS CIENTÍFICOS
%------------------------------------------------------------------------------
\pagestyle{fancy}
\setlength{\headheight}{14pt}

\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\lhead{\footnotesize \textsc{L. Romero Mascaró}}
\rhead{\footnotesize \textit{Relajación Bidireccional y Poda Geométrica en Digrafos Triangulares}}
\cfoot{\small \thepage\ de \pageref*{LastPage}}

\fancypagestyle{firststyle}{
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0.4pt}
  \cfoot{\small \thepage\ de \pageref*{LastPage}}
}

%------------------------------------------------------------------------------
%	BLOQUE DE TÍTULO / ENCABEZADO FORMAL
%------------------------------------------------------------------------------
\renewcommand*{\maketitle}{
  \thispagestyle{firststyle}
  \begin{center}
    \vspace*{0.3cm}
    {\LARGE \bfseries Relajación Bidireccional In-Place y Poda por Dominancia Geométrica para Caminos Mínimos en Digrafos Planares Triangulares\par}
    \vspace{0.8cm}
    
    {\large \textbf{Lucio Romero Mascaró}}\\[0.15cm]
    {\normalsize Investigador Independiente}\\[0.1cm]
    {\small \texttt{lucioromeromascaro@gmail.com} \quad\textbar\quad \texttt{github.com/lucio-rm}}\\[0.3cm]
    
    {\small \today}\\[0.4cm]
    \rule{\textwidth}{0.5pt}
  \end{center}
  \vspace{0.1cm}
}
