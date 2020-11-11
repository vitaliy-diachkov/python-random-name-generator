import pytest
from click.testing import CliRunner

from random_name_generator.cli import generate_random_names


@pytest.mark.usefixtures(
    'mock_first_names',
    'mock_last_names',
    'mock_random_shuffle'
)
class TestCommandLineInterface():

    @classmethod
    def setup_class(cls):
        cls.runner = CliRunner()

    @pytest.mark.parametrize(
        'options,expected_output',
        [
            (['--limit=1'], 'Alex Abramson\n'),
            (['--limit', 1], 'Alex Abramson\n'),
            (['-L', 1], 'Alex Abramson\n'),
            (['-D', 'English', '--limit=1'], 'Alex Abramson\n'),
            (['-D', 'English', '--limit=1'], 'Alex Abramson\n'),
            (['-D', 'ENGLISH', '--limit=1'], 'Alex Abramson\n'),
            (
                ['-D', 'English', '-S', 'male', '--limit=2'],
                'Alex Abramson\nJohn Johnson\n'
            ),
            (
                ['-D', 'English', '-S', 'Male', '--limit=2'],
                'Alex Abramson\nJohn Johnson\n'
            ),
            (
                ['-D', 'English', '-S', 'MALE', '--limit=2'],
                'Alex Abramson\nJohn Johnson\n'
            ),
            (['-D', 'English/English', '--limit=1'], 'Alex Abramson\n'),
            (['-D', 'English/Italian', '--limit=1'], 'Alex Gotti\n'),
            (['-D', 'Italian', '-L', 1], 'Cosme Gotti\n')
        ]
    )
    def test_cli_with_parameters(self, options, expected_output):
        result = self.runner.invoke(generate_random_names, options)
        assert result.exit_code == 0
        assert result.output == expected_output

    @pytest.mark.parametrize(
        'options,output_fragment,max_possible_count',
        [
            (['--limit=999'], '999 unisex English', 1),
            (
                ['-D', 'English/English', '--limit=999'],
                '999 unisex English',
                1
            ),
            (
                ['-D', 'English', '-S', 'male', '--limit=999'],
                '999 male English',
                2
            ),
            (
                ['-D', 'English/Italian', '--limit=999'],
                '999 unisex English/Italian',
                1
            )
        ]
    )
    def test_cli_limit_exceeded(
        self,
        options,
        output_fragment,
        max_possible_count
    ):
        result = self.runner.invoke(generate_random_names, options)
        assert result.output == (
            'We can not generate {options_str} names (max. possible '
            'count: {count}).\n'
        ).format(
            options_str=output_fragment,
            count=max_possible_count
        )

    @pytest.mark.parametrize('descent', [
        'polish',
        'Polish',
        'POLISH',
        'English/POLISH',
        'Polish/English'
    ])
    def test_cli_invalid_descent(self, descent):
        result = self.runner.invoke(
            generate_random_names,
            ['-D', descent, '--limit=1']
        )

        assert result.output == f'Invalid descent: {descent}.\n'

    @pytest.mark.parametrize('sex', ['man', 'woman', 'allien'])
    def test_cli_invalid_sex(self, sex):
        result = self.runner.invoke(
            generate_random_names,
            ['-S', sex, '-L', 1]
        )

        assert result.output == f'Invalid sex: {sex}.\n'

    @pytest.mark.parametrize(
        'descent',
        ['French', 'French/English', 'English/German']
    )
    def test_cli_unsupported_descent(self, descent):
        result = self.runner.invoke(
            generate_random_names,
            ['-D', descent, '-L', 1]
        )

        assert result.output == f'Unsupported descent: {descent}.\n'

    @pytest.mark.parametrize(
        'options,expected_output',
        [
            (
                ['-D', 'German', '-L', 1],
                'German descent does not support unisex sex.\n'
            ),
            (
                ['-D', 'German', '-S', 'male', '-L', 1],
                'German descent does not support male sex.\n'
            ),
            (
                ['-D', 'German/English', '-L', 1],
                'German/English descent does not support unisex sex.\n'
            ),
            (
                ['-D', 'Russian', '-L', 1],
                'Russian descent does not support unisex sex.\n'
            )
        ]
    )
    def test_cli_unsupported_sex(self, options, expected_output):
        result = self.runner.invoke(generate_random_names, options)
        assert result.output == expected_output
