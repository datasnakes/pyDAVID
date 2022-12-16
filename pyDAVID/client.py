import requests
from typing import List, Union

class DavidAnnotator:
    """
    A class for annotating IDs using the DAVID functional annotation API.
    """
    
    DAVID_API_ENDPOINT = 'https://david.ncifcrf.gov/api.jsp'
    
    def __init__(self, id_type: str, tool: str='chartReport', fields: List[str]='', species: str='9606'):
        """
        Initialize a DavidAnnotator object.
        
        Parameters:
        - id_type: the type of IDs to annotate (e.g. 'ENSEMBL_GENE_ID')
        - tool: the tool to use for annotation (defaults to 'chartReport')
        - fields: a list of fields to include in the annotation (defaults to all fields)
        - species: the species for the IDs (defaults to human, i.e. '9606')
        """
        self.id_type = id_type
        self.tool = tool
        self.fields = fields
        self.species = species
    
    def annotate(self, ids: List[str]) -> Union[dict, None]:
        """
        Annotate a list of IDs.
        
        Parameters:
        - ids: a list of IDs (strings) to annotate
        
        Returns:
        - A dictionary with the annotation results, or None if an error occurred.
        """
        params = {
            'ids': ','.join(ids),
            'idType': self.id_type,
            'tool': self.tool,
            'fields': ','.join(self.fields),
            'species': self.species
        }
        response = requests.get(self.DAVID_API_ENDPOINT, params=params)
        
        if response.status_code != 200:
            return None
        
        return response.json()
