import re

with open('Sections/2.Relatedwork.tex', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    r'\[1\]': r'\\cite{cox1999_maximizing}',
    r'\[2\]': r'\\cite{borel2004_topology}',
    r'\[3\]': r'\\cite{jensen2011_topology}',
    r'\[4\]': r'\\cite{lalaukeraly2013_adjoint}',
    r'\[5\]': r'\\cite{piggott2015_inverse_design}',
    r'\[6\]': r'\\cite{shen2015_integrated_pbs}',
    r'\[7\]': r'\\cite{frellsen2016_topology_mdm}',
    r'\[8\]': r'\\cite{piggott2017_fabrication}',
    r'\[9\]': r'\\cite{molesky2018_inverse}',
    r'\[10\]': r'\\cite{hammond2021_photonic}',
    r'\[11\]': r'\\cite{pao2026_nano}',
    r'\[12\]': r'\\cite{kirkpatrick1983_simulated_annealing}',
    r'\[13\]': r'\\cite{kadowaki1998_quantum_annealing}',
    r'\[14\]': r'\\cite{rendle2010_factorization}',
    r'\[15\]': r'\\cite{kitai2020_fmqa}',
    r'\[16\]': r'\\cite{inoue2022_fmqa_pcsel}',
    r'\[17\]': r'\\cite{zhu2024_machine_learning}',
    r'\[18\]': r'\\cite{hu2025_optical_filter}',
    r'\[19\]': r'\\cite{chang2026_quantum_compatible}',
    r'\[20\]': r'\\cite{lazarov2011_filters}',
    r'\[21\]': r'\\cite{odena2016_deconvolution}',
    r'\[22\]': r'\\cite{shi2016_subpixel_cnn}',
    r'\[23\]': r'\\cite{higgins2017_betavae}',
    r'\[24\]': r'\\cite{piggott2017_fabrication}',
    r'\[25\]': r'\\cite{burgess2018_understanding_betavae}',
    r'\[26\]': r'\\cite{ma2019_probabilistic}',
    r'\[27\]': r'\\cite{zhang2019_shift_invariant}',
    r'\[28\]': r'\\cite{li2020_fourier_neural_operator}',
    r'\[29\]': r'\\cite{kudyshev2021_machine_learning}',
    r'\[30\]': r'\\cite{karras2021_alias_free}',
    r'\[5, 6\]': r'\\cite{piggott2015_inverse_design,shen2015_integrated_pbs}',
    r'\[11\]\s*extbf\{2026年\}': r'\\cite{pao2026_nano}\\textbf{2026年}',
}

for k, v in replacements.items():
    text = re.sub(k, v, text)

with open('Sections/2.Relatedwork.tex', 'w', encoding='utf-8') as f:
    f.write(text)

with open('Sections/3.Theory.tex', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('經典著作 [29]', '經典著作 \\cite{yariv2007_photonics}')
text = text.replace('分析架構 [29]', '分析架構 \\cite{yariv2007_photonics}')

with open('Sections/3.Theory.tex', 'w', encoding='utf-8') as f:
    f.write(text)
