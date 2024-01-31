from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

demo_table = resource('dynamodb').Table('user')

def insert():
    print("Inserting a new item:")
    
    user_id = input("Enter user_id: ")
    customer_id = input("Enter customer_id: ")
    order_id = input("Enter order_id: ")
    status = input("Enter status: ")

    response = demo_table.put_item(
        Item={
            'user_id': user_id,
            'customer_id': customer_id,
            'order_id': order_id,
            'status': status,
            'created_date': datetime.now().isoformat()
        }
    )

    print(f'Insert response: {response}')
    print("Item inserted successfully.")

def delete():
    print("Deleting transactions")
    user_ids_input = input("Enter user_ids separated by space: ")
    delete_ids = user_ids_input.split()

    with demo_table.batch_writer() as batch:
        for user_id in delete_ids:
            response = batch.delete_item(Key={"user_id": user_id})

    print("Items deleted successfully.")

def update_user():
    user_id = input("Enter the user_id of the item to update: ")
    response = demo_table.query(KeyConditionExpression=Key('user_id').eq(user_id))
    items = response.get('Items', [])

    if not items:
        print(f"Item with user_id {user_id} not found.")
        return

    existing_item = items[0]

    update_customer_id = input("Do you want to update customer_id? (yes/no): ")
    new_customer_id = input("Enter the new customer_id: ") if update_customer_id.lower() == 'yes' else existing_item['customer_id']

    update_order_id = input("Do you want to update order_id? (yes/no): ")
    new_order_id = input("Enter the new order_id: ") if update_order_id.lower() == 'yes' else existing_item['order_id']

    new_name = input("Enter the new name: ")

    demo_table.put_item(
        Item={
            'user_id': new_name,
            'customer_id': new_customer_id,
            'order_id': new_order_id,
            'status': existing_item['status'],
            'created_date': datetime.now().isoformat()
        }
    )

    demo_table.delete_item(Key={'user_id': user_id})

    print("Item updated successfully.")

def display_all_items():
    print("Displaying all items in the 'user' table:")
    response = demo_table.scan()
    items = response.get('Items', [])

    for item in items:
        print("User ID:", item.get('user_id'))
        print("Created Date:", item.get('created_date'))
        print("Customer ID:", item.get('customer_id'))
        print("Order ID:", item.get('order_id'))
        print("Status:", item.get('status'))
        print()

def main_menu():
    while True:
        print("\nOptions:")
        print("1. Insert Item")
        print("2. Delete Item")
        print("3. Update Item")
        print("4. Display All Items")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert()
        elif choice == '2':
            delete()
        elif choice == '3':
            update_user()
        elif choice == '4':
            display_all_items()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        another_operation = input("Do you want to perform another operation? (yes/no): ").lower()
        if another_operation != 'yes':
            break

# Run the main menu
main_menu()
