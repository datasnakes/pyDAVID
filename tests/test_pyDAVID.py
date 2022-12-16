import unittest

class TestDavidAnnotator(unittest.TestCase):
    def test_annotate(self):
        annotator = DavidAnnotator('ENSEMBL_GENE_ID')
        
        # Test annotation of a single ID
        ids = ['ENSG00000139618']
        annotation = annotator.annotate(ids)
        self.assertIsInstance(annotation, dict)
        self.assertIn('annotation', annotation)
        
        # Test annotation of multiple IDs
        ids = ['ENSG00000139618', 'ENSG00000169083', 'ENSG00000198712']
        annotation = annotator.annotate(ids)
        self.assertIsInstance(annotation, dict)
        self.assertIn('annotation', annotation)
        
        # Test annotation of IDs with a specific tool
        annotator = DavidAnnotator('ENSEMBL_GENE_ID', tool='overRepresentation')
        annotation = annotator.annotate(ids)
        self.assertIsInstance(annotation, dict)
        self.assertIn('annotation', annotation)
        
        # Test annotation of IDs with specific fields
        annotator = DavidAnnotator('ENSEMBL_GENE_ID', fields=['GO_BP', 'GO_CC'])
        annotation = annotator.annotate(ids)
        self.assertIsInstance(annotation, dict)
        self.assertIn('annotation', annotation)
        
        # Test annotation of IDs from a different species
        annotator = DavidAnnotator('ENSEMBL_GENE_ID', species='10090')
        annotation = annotator.annotate(ids)
        self.assertIsInstance(annotation, dict)
        self.assertIn('annotation', annotation)
        
        # Test annotation of invalid IDs
        ids = ['INVALID_ID']
        annotation = annotator.annotate(ids)
        self.assertIsNone(annotation)

if __name__ == '__main__':
    unittest.main()
