
SELECT 
    "NomTitularEmpreendimento",
    "NomMunicipio",
    "NumCPFCNPJ",
    SUM("MdaPotenciaInstaladaKW") AS potencia_total,
    COUNT(*) AS qtd_empreendimentos
FROM empreendimentos_pe AS e
GROUP BY "NomTitularEmpreendimento", "NomMunicipio", "NumCPFCNPJ"
HAVING SUM("MdaPotenciaInstaladaKW") > 75
ORDER BY potencia_total DESC 
