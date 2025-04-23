from tests.mock_project.user_service import create_user, initialize_app, update_user


def run_app():
    """Main application entry point"""
    initialize_app()
    
    # Create a user
    user_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    
    user_id = create_user(user_data)
    print(f"Created user with ID: {user_id}")
    
    # Update a user
    update_data = {
        "name": "John Updated",
        "email": "john.updated@example.com"
    }
    
    updated_id = update_user(user_id, update_data)
    print(f"Updated user with ID: {updated_id}")
    
    return True


if __name__ == "__main__":
    run_app() 