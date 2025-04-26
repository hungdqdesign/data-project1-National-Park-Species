# National Park Dataset Metadata

## Dataset Information
**Title**: Most Visited National Parks Species Data  
**Source**: [Tidytuesday - National Parks Species Dataset](https://github.com/rfordatascience/tidytuesday/blob/main/data/2024/2024-10-08/readme.md)  
**Date**: October 8, 2024  
**Description**: This dataset contains information about species observed in U.S. National Parks. It includes details on species categories, families, scientific names, common names, conservation statuses, and other relevant attributes related to species observations.

## Provenance
The dataset was sourced from the **Tidytuesday** project, which aggregates various datasets for data science and visualization challenges. The information is collected from multiple National Park Service sources and other conservation-related databases.

## Codebook

| Column Name          | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **ParkCode**         | A unique identifier for the park.                                            |
| **ParkName**         | Name of the National Park.                                                   |
| **CategoryName**     | The category of the species (e.g., Mammal, Bird).                           |
| **Order**            | The biological order the species belongs to.                                 |
| **Family**           | The biological family of the species.                                        |
| **TaxonRecordStatus**| The status of the taxon record (e.g., Active).                              |
| **SciName**          | The scientific (Latin) name of the species.                                  |
| **CommonNames**      | Common names of the species.                                                 |
| **Synonyms**         | Alternate names or synonyms for the species.                                |
| **ParkAccepted**     | Boolean indicating if the species is accepted in the park.                  |
| **ParkTags**         | Additional park-specific tags related to the species.                       |
| **References**       | References or citations related to the species.                             |
| **Observations**     | The number of observations for this species in the park.                    |
| **Vouchers**         | The number of vouchers related to the species.                              |
| **ExternalLinks**    | Links to external resources for more information on the species.            |
| **TEStatus**         | The species' status with respect to being threatened or endangered.         |
| **StateStatus**      | The state-level conservation status of the species.                         |
| **OzoneSensitiveStatus** | Indicates the species' sensitivity to ozone levels.                      |
| **GRank**            | The global conservation status rank of the species.                         |
| **SRank**            | The state-level conservation status rank of the species.                    |

## Notes
- The dataset includes both common and scientific names of species, as well as the conservation status and observation details for each species in various national parks.
- Columns like **GRank** and **SRank** provide insights into the global and state-level conservation status of species.
- The dataset is intended for use in ecological, conservation, and biodiversity research.

## License
This dataset is provided under the terms of the [Open Data License](https://opendatacommons.org/licenses/odbl/1-0/).
