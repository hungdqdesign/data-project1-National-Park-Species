# National Park Species Dataset Analysis

## Introduction

The dataset provides information on species observed in the 15 most visited parks in the USA. The information includes park name, species name, numbers observed, conservation status, etc. This is a portion of the data extracted from a centralized online platform developed by the U.S. National Park Service (NPS). Its main purpose is to provide access to a wide range of natural and cultural resource data and information related to national parks across the United States.

With information on species in the park, surveys can be conducted to see how rich the flora and fauna are, and the number of individuals observed can be used to verify food chain theories or investigate abnormalities in the ecosystem. The conservation status of species can also be investigated to find ways to conserve and restore the ecosystem.

One problem with the dataset is that there is no time series for the recorded data, so it is difficult to detect trends in changes in fauna and flora or to combine the dataset with time-varying data such as CO2 levels. The dataset also does not have the location of the park, so if you want to survey vegetation based on geographic location, you will need to consult another data source.

---

## Question 1: Does the species data from 15 most visited parks reflect the pyramid of number/biomass (Food chain pyramid)?

### Introduction

Based on studies and observations, food chains indicate that the higher an animal is in the chain, the fewer individuals there are — and vice versa. Our group found that it is possible to use observational data from the dataset to support this theory.

We extracted key information relevant to the question, including the national park name (`ParkName`), species category name (`CategoryName`), common name of the species (`CommonNames`), and the number of observed individuals (`References`). With this data, we were able to create graphs illustrating the population of each species and evaluate whether the results align with the concept of the pyramid of numbers.

### Approach

To make the chart interactive and visually engaging, we created multiple charts using Dash (Python) and Power BI. The main chart is a scatter plot that shows the correlation between species names and the number of individuals observed. We chose a scatter plot because it effectively illustrates the relationship between two variables — in this case, species name and the number of individuals.

Species categories are treated as categorical variables, and we matched them to their respective food chain levels using species overview data from Wikipedia. The scatter plot also includes regression lines to highlight trends between the number of species and their types based on reference numbers.

Additionally, we use a bar chart to display the top 10 most common species names when a specific species is selected in the scatter plot. This feature enhances interactivity and allows readers to explore each species in more detail and understand its position within the food chain.

### Analysis

Code and analysis files: [GitHub Repository](https://github.com/hungdqdesign/data-project1-National-Park-Species)

### Discussion

Some conclusions that can be drawn after observing and analyzing the graph are as follows:

- The number of species in the scatter plot reflects the nature of the food chain pyramid: the higher a species is in the food chain, the fewer individuals there are. The regression line drawn from the data also supports this trend.
- However, there are outliers, such as Yellowstone National Park, which shows a species distribution that deviates from the typical food chain pattern. This suggests either a bias in data recording for this park or a unique characteristic in the distribution of flora and fauna there.
- When analyzing the most common species in the bar chart, some species are not placed correctly within the food chain. For example, mule deer and deer mice are listed as mammals and, due to a coarse classification system, are ranked at the top of the chain — even though they are herbivores and not typically top-level predators.
- This highlights the need for more detailed species classification to create a food chain hierarchy that more accurately reflects natural ecosystems.

---

## Question 2: What proportion of species are endangered, threatened, or of special concern?

### Introduction

Conservation of biodiversity is a critical mission of the National Park Service. Understanding which species are at risk and how they are distributed across different parks is essential for effective conservation management. This analysis explores the proportion of species classified as endangered, threatened, or of special concern within the most visited national parks in the United States using the NPS Species dataset.

The dataset contains comprehensive information on 61,119 species documented across 15 major national parks, including their taxonomic classification and conservation status. This question identifying conservation patterns across different species categories and park locations can highlight where conservation efforts are most urgently needed and help evaluate the effectiveness of existing protection measures.

### Approach

To analyze the proportion of species with vulnerable conservation status, we create three complementary visualizations:

1. **Stacked Bar Chart**: Shows the proportion of species in each conservation status category (endangered, threatened, special concern, and other) across different biological taxonomic groups. The stacked nature of the bars allows us to see both the total proportion of at-risk species and the breakdown by severity level.

2. **Horizontal Bar Chart**: Shows the correlation between species categories and conservation status. For example, birds have a negative correlation (-0.1613) with total biodiversity, while insects and other invertebrates have very strong positive correlations (>0.99). This chart helps identify which taxonomic groups might have disproportionate conservation concerns.

3. **Bubble Chart**: Analyzes conservation status by region and ecosystem type. Inspired by the species richness chart, it highlights that while regions like the Appalachian temperate forests have high species richness, ecosystems like Desert/Canyon or Alpine/Subalpine might have higher percentages of vulnerable species despite lower total species counts.

### Analysis

GitHub: [https://github.com/hungdqdesign/data-project1-National-Park-Species](https://github.com/hungdqdesign/data-project1-National-Park-Species)

### Python Code for Question 1

_See code in GitHub repository linked above._

### Discussion

- Birds have the highest proportion of conservation concerns despite their negative correlation with total biodiversity, suggesting they face disproportionate challenges.
- While the Appalachian region's temperate forests have the highest species richness, Desert/Canyon ecosystems in the Southwest and Alpine/Subalpine ecosystems in the Rocky Mountains show higher percentages of vulnerable species.
- This highlights that biodiversity hotspots aren't necessarily conservation priority hotspots — specialized species in extreme environments often face greater threats due to narrow ecological niches.
- Overall, about **4-5% of species have conservation concerns**, varying significantly across taxonomic groups, regions, and ecosystems.

---

## Conclusion

Our analysis of the National Park Service dataset confirmed the food chain pyramid theory while identifying that about **4-5% of species face conservation concerns**, with birds being disproportionately vulnerable.

We discovered that biodiversity hotspots don't necessarily align with conservation priorities — specialized Desert/Canyon and Alpine/Subalpine ecosystems show higher percentages of threatened species than species-rich temperate forests.

### Recommendations

- Implement more detailed species classification systems
- Develop targeted conservation strategies for birds
- Allocate additional resources to specialized ecosystems with high vulnerability rates
- Conduct temporal studies to track population changes
- Incorporate geographic data
- Investigate outlier parks like Yellowstone for unique ecological patterns or data collection issues

**Note**: The dataset does not have information about the time of species recording — only static information — so it is difficult to combine with another dataset such as atmospheric CO2 over time to track the correlation between vegetation and CO2. Plants are very sensitive to this variable.

