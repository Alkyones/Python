import csv
import argparse
from faker import Faker
import sys
from typing import List, Dict, Any

class FakeDataGenerator:
    """A class to generate fake data for specified columns using Faker library."""
    
    def __init__(self, locale='en_US'):
        """Initialize the Faker instance with specified locale."""
        self.fake = Faker(locale)
        
        # Define mapping of column types to Faker methods
        self.column_mappings = {
            'first_name': lambda: self.fake.first_name(),
            'last_name': lambda: self.fake.last_name(),
            'full_name': lambda: self.fake.name(),
            'email': lambda: self.fake.email(),
            'phone': lambda: self.fake.phone_number(),
            'address': lambda: self.fake.address(),
            'street_address': lambda: self.fake.street_address(),
            'city': lambda: self.fake.city(),
            'state': lambda: self.fake.state(),
            'zip_code': lambda: self.fake.zipcode(),
            'country': lambda: self.fake.country(),
            'company': lambda: self.fake.company(),
            'job_title': lambda: self.fake.job(),
            'ssn': lambda: self.fake.ssn(),
            'date_of_birth': lambda: self.fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
            'credit_card': lambda: self.fake.credit_card_number(),
            'username': lambda: self.fake.user_name(),
            'password': lambda: self.fake.password(),
            'website': lambda: self.fake.url(),
            'ip_address': lambda: self.fake.ipv4(),
            'uuid': lambda: self.fake.uuid4(),
            'license_plate': lambda: self.fake.license_plate(),
            'color': lambda: self.fake.color_name(),
            'text': lambda: self.fake.text(max_nb_chars=200),
            'sentence': lambda: self.fake.sentence(),
            'paragraph': lambda: self.fake.paragraph(),
            'number': lambda: self.fake.random_int(min=1, max=1000),
            'float': lambda: round(self.fake.random.uniform(0, 100), 2),
            'boolean': lambda: self.fake.boolean(),
            'currency': lambda: f"${self.fake.random_int(min=10, max=10000)}.{self.fake.random_int(min=10, max=99)}",
            'age': lambda: self.fake.random_int(min=18, max=80),
            'department': lambda: self.fake.random_element(elements=('HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'Operations')),
            'bank_account': lambda: self.fake.bban(),
        }
    
    def get_available_columns(self) -> List[str]:
        """Return a list of available column types."""
        return list(self.column_mappings.keys())
    
    def generate_data(self, columns: List[str], num_rows: int) -> List[Dict[str, Any]]:
        """
        Generate fake data for specified columns.
        
        Args:
            columns: List of column names/types
            num_rows: Number of rows to generate
            
        Returns:
            List of dictionaries containing the generated data
        """
        data = []
        
        for _ in range(num_rows):
            row = {}
            for column in columns:
                if column.lower() in self.column_mappings:
                    row[column] = self.column_mappings[column.lower()]()
                else:
                    # If column type not found, generate generic text
                    row[column] = self.fake.word()
            data.append(row)
        
        return data
    
    def save_to_csv(self, data: List[Dict[str, Any]], filename: str):
        """
        Save generated data to CSV file.
        
        Args:
            data: List of dictionaries containing the data
            filename: Output CSV filename
        """
        if not data:
            print("No data to save.")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        
        print(f"Data saved to {filename}")

def main():
    """Main function to handle command line arguments and generate fake data."""
    parser = argparse.ArgumentParser(description='Generate fake data for specified columns using Faker library')
    parser.add_argument('--columns', '-c', nargs='+', required=True, 
                        help='Column names/types to generate data for')
    parser.add_argument('--rows', '-r', type=int, default=100, 
                        help='Number of rows to generate (default: 100)')
    parser.add_argument('--output', '-o', default='fake_data.csv', 
                        help='Output CSV filename (default: fake_data.csv)')
    parser.add_argument('--locale', '-l', default='en_US', 
                        help='Faker locale (default: en_US)')
    parser.add_argument('--list-columns', action='store_true', 
                        help='List all available column types')
    
    args = parser.parse_args()
    
    # Initialize the fake data generator
    generator = FakeDataGenerator(locale=args.locale)
    
    # If user wants to see available columns
    if args.list_columns:
        print("Available column types:")
        for column in sorted(generator.get_available_columns()):
            print(f"  - {column}")
        return
    
    try:
        # Generate fake data
        print(f"Generating {args.rows} rows of fake data for columns: {', '.join(args.columns)}")
        data = generator.generate_data(args.columns, args.rows)
        
        # Save to CSV
        generator.save_to_csv(data, args.output)
        
        # Display first few rows as preview
        print(f"\nPreview of first 3 rows:")
        for i, row in enumerate(data[:3]):
            print(f"Row {i+1}: {row}")
            
    except Exception as e:
        print(f"Error generating data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage when run directly
    if len(sys.argv) == 1:
        # No command line arguments, show example usage
        print("Fake Data Generator")
        print("==================")
        print("\nExample usage:")
        print("python fake_people_csv.py --columns first_name last_name email --rows 50")
        print("python fake_people_csv.py -c full_name phone address city --rows 200 -o people.csv")
        print("python fake_people_csv.py --list-columns")
        print("\nRunning example with default settings...")
        
        # Generate example data
        generator = FakeDataGenerator()
        example_columns = ['first_name', 'last_name', 'email', 'phone', 'city']
        data = generator.generate_data(example_columns, 10)
        generator.save_to_csv(data, 'example_fake_data.csv')
        print(f"\nExample data generated with columns: {', '.join(example_columns)}")
    else:
        main()