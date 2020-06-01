import click
import csv

DENORMALIZE_COLUMNS = [
    'chicago_phase_2',
    'chicago_phase_3',
    'phase_1',
    'phase_2',
    'phase_3',
    'phase_4',
    'phase_5'
]


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def transpose(input, output):
    """Generate a schema"""
    output_data = []

    reader = csv.DictReader(input)

    for row in reader:
        for col in DENORMALIZE_COLUMNS:
            col_parts = col.split('_')
            status_col = f'{col}_status'

            if col_parts[0] == 'chicago':
                scope = 'Chicago'
            else:
                scope = 'Illinois'

            phase = ' '.join(col_parts[-2:])

            value = row[col]

            if value:
                output_data.append({
                    'scope': scope,
                    'phase': phase,
                    'activity': row.get('activity'),
                    'status': value,
                    'status_color': row[status_col],
                })

    writer = csv.DictWriter(output, fieldnames=output_data[0].keys())
    writer.writeheader()
    writer.writerows(output_data)


if __name__ == '__main__':
    transpose()
