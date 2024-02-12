from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

demo_table = resource('dynamodb').Table('test')

def insert():
    print("Inserting a new item:")
    
    while True:
        user_id = int(input("Enter user_id: ")) 
        response = demo_table.query(KeyConditionExpression=Key('id').eq(user_id))
        items = response.get('Items', [])
        if items:
            print("User ID already exists. Please choose a different ID.")
        else:
            break

    customer_name = input("Enter customer name: ") 

    response = demo_table.scan(Select='COUNT')
    count = response['Count']
    order_id = count + 1
    
    while True:
        status = input("Enter status (pending/done): ")
        if status.lower() not in ['pending', 'done']:
            print("Invalid status! Please enter 'pending' or 'done'.")
        else:
            break

    response = demo_table.put_item(
        Item={
            'id': user_id,
            'customer_name': customer_name,  
            'order_id': order_id,
            'status': status.lower(),  
            'created_date': datetime.now().isoformat()
        }
    )

    print(f'Insert response: {response}')
    print("Item inserted successfully.")

def delete():
    print("Deleting transactions")
    user_ids_input = input("Enter user_ids: ")
    delete_ids = user_ids_input.split()

    with demo_table.batch_writer() as batch:
        for user_id in delete_ids:
            response = batch.delete_item(Key={"id": int(user_id)})  
    print("Items deleted successfully.")

def update_user():
    user_id = int(input("Enter the user_id of the item to update: "))  
    response = demo_table.query(KeyConditionExpression=Key('id').eq(user_id))
    items = response.get('Items', [])

    if not items:
        print(f"Item with user_id {user_id} not found.")
        return

    existing_item = items[0]

    update_customer_name = input("Do you want to update customer name? (yes/no): ")
    new_customer_name = input("Enter the new customer name: ") if update_customer_name.lower() == 'yes' else existing_item['customer_id']

    update_order_id = input("Do you want to update order_id? (yes/no): ")
    new_order_id = input("Enter the new order_id: ") if update_order_id.lower() == 'yes' else existing_item['order_id']

    demo_table.put_item(
        Item={
            'id': user_id, 
            'customer_name': new_customer_name,  
            'order_id': new_order_id,
            'status': existing_item['status'],
            'created_date': datetime.now().isoformat()
        }
    )

    print("Item updated successfully.")

def display_all_items():
    print("Displaying all items in the 'user' table:")
    response = demo_table.scan()
    items = response.get('Items', [])

    for item in items:
        print("-----------------------------------------------------")
        print("ID:", item.get('id'))  
        print("Created Date:", item.get('created_date')) 
        print("Customer Name:", item.get('customer_name')) 
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

main_menu()
