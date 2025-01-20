<?php

namespace App\Services;

use App\Models\User;

class UserManager
{
    /**
     * Get a list of all users.
     *
     * @return array
     */
    public function getAllUsers(): array
    {
        // Mocked list of users
        return [
            ['id' => 1, 'name' => 'John Doe', 'email' => 'john.doe@example.com'],
            ['id' => 2, 'name' => 'Jane Smith', 'email' => 'jane.smith@example.com'],
        ];
    }

    /**
     * Add a new user to the database.
     *
     * @param string $name
     * @param string $email
     * @return bool
     */
    public function addUser(string $name, string $email): bool
    {
        // Simulate adding a user to the database
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("Invalid email address provided.");
        }

        // Normally, this would involve database operations
        echo "User added successfully: $name <$email>\n";
        return true;
    }

    /**
     * Delete a user by ID.
     *
     * @param int $id
     * @return bool
     */
    public function deleteUser(int $id): bool
    {
        // Simulate deleting a user
        echo "User with ID $id deleted successfully.\n";
        return true;
    }
}

// Example usage
try {
    $userManager = new UserManager();

    // Fetch all users
    $users = $userManager->getAllUsers();
    print_r($users);

    // Add a new user
    $userManager->addUser('Alice Johnson', 'alice.johnson@example.com');

    // Delete a user
    $userManager->deleteUser(1);
} catch (\Exception $e) {
    echo "Error: " . $e->getMessage();
}
