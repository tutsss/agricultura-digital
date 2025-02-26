# Carregar dados simulados
dados <- data.frame(
  cultura = c("Soja", "Milho"),
  area = c(500, 300),
  insumos = c(250, 180)
)

# Calcular estatísticas básicas
media_area <- mean(dados$area)
desvio_area <- sd(dados$area)

media_insumos <- mean(dados$insumos)
desvio_insumos <- sd(dados$insumos)

# Exibir resultados
cat("Média da área plantada:", media_area, "\n")
cat("Desvio padrão da área plantada:", desvio_area, "\n")
cat("Média do uso de insumos:", media_insumos, "\n")
cat("Desvio padrão do uso de insumos:", desvio_insumos, "\n")
