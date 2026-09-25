
SELECT
    titular,
    municipio,
    cpf_cnpj,
    fonte,
    classe,
    subgrupo,
    SUM(potencia_kw) AS potencia_total,
    COUNT(*) AS qtd_empreendimentos
FROM empreendimentos_pe AS e
WHERE distribuidora = 'Neoenergia PE' AND uf = 'PE'
GROUP BY titular, municipio, cpf_cnpj, fonte, classe, subgrupo
HAVING SUM(potencia_kw) > 75
ORDER BY potencia_total DESC
