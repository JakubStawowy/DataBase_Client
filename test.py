import unittest
from project_model import ProjectModel
from table import Table


class TestProjectModel(unittest.TestCase):
    """
    TestProjectModel class
    """
    def test_add_table(self):
        test_table = Table('test_table', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                           [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])
        project_model = ProjectModel()
        project_model.add_table(test_table)

        self.assertEqual(str(test_table), str(project_model.get_table('test_table')))

    def test_remove_table(self):
        test_table_1 = Table('test_table_1', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                             [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])
        test_table_2 = Table('test_table_2', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                             [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])

        project_model = ProjectModel()

        project_model.add_table(test_table_1)
        project_model.add_table(test_table_2)

        project_model.remove_table('test_table_1')

        self.assertNotIn(test_table_1, project_model.get_structure())
        self.assertIn(test_table_2, project_model.get_structure())

    def test_add_row(self):
        test_table_1 = Table('test_table_1', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                             [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])
        project_model = ProjectModel()

        project_model.add_table(test_table_1)

        project_model.add_row('test_table_1', [4, 'row_4'])

        self.assertEqual(project_model.get_table('test_table_1').get_number_of_rows(), 4)

    def test_edit_row(self):
        test_table_1 = Table('test_table_1', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                             [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])
        project_model = ProjectModel()

        project_model.add_table(test_table_1)

        project_model.edit_row('test_table_1', [2, 'row_2'], [2, 'row_2_edited'])

        edited_row = project_model.get_table('test_table_1').get_row(1)

        self.assertEqual(edited_row, [2, 'row_2_edited'])

    def test_lambda(self):
        project_model = ProjectModel()
        project_model.add_table(Table('test_table', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                                      [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']]))

        lambda_expression = project_model.generate_lambda_expression('test_table')

        self.assertNotEqual(lambda_expression, None)

        records_1 = project_model.lambda_browse('test_table', lambda_expression)

        self.assertGreaterEqual(len(records_1), 0)

        records_2 = project_model.lambda_browse('test_table', 'lambda col_1:col_1>1')

        self.assertEqual(records_2, [[2, 'row_2'], [3, 'row_3']])

    def test_file(self):
        table_attributes = ('test_table', 2, 3, {'col_1': 'Liczba całkowita', 'col_2': 'Tekst'},
                            [[1, 'row_1'], [2, 'row_2'], [3, 'row_3']])
        table_to_save = Table(*table_attributes)
        project_model_1 = ProjectModel()
        project_model_1.add_table(table_to_save)

        project_model_1.write_to_file('test_file.txt')

        project_model_2 = ProjectModel()
        project_model_2.read_from_file('test_file.txt')

        get_table = project_model_2.get_table('test_table')

        self.assertEqual(str(table_to_save), str(get_table))


if __name__ == '__main__':
    unittest.main()
