<?php
header('Content-Type: application/json');

$servername = getenv('DB_HOST');
$username = getenv('DB_USER');
$password = getenv('DB_PASS');
$dbname = getenv('DB_NAME');

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo json_encode(["message" => "Connection successful!"]);
} catch (PDOException $e) {
    echo json_encode(["error" => "Connection failed: " . $e->getMessage()]);
    exit;
}

$endpoint = isset($_GET['endpoint']) ? $_GET['endpoint'] : '';

switch ($_SERVER['REQUEST_METHOD']) {
    case 'GET':
        if ($endpoint === 'orders') {
            $stmt = $conn->prepare("SELECT * FROM orders");
            $stmt->execute();
            $orders = $stmt->fetchAll(PDO::FETCH_ASSOC);
            echo json_encode($orders);
        }
        break;

    case 'POST':
        if ($endpoint === 'orders') {
            $data = json_decode(file_get_contents("php://input"), true);
            if (!isset($data['book_id'], $data['user_id'], $data['status'])) {
                echo json_encode(['error' => 'Missing required fields']);
                exit;
            }
            $stmt = $conn->prepare("INSERT INTO orders (book_id, user_id, status) VALUES (?, ?, ?)");
            $stmt->execute([$data['book_id'], $data['user_id'], $data['status']]);
            echo json_encode(['message' => 'Order added successfully']);
        }
        break;

    case 'DELETE':
        if (isset($_GET['order_id'])) {
            $order_id = $_GET['order_id'];
            $stmt = $conn->prepare("DELETE FROM orders WHERE id = ?");
            $stmt->execute([$order_id]);
            echo json_encode(['message' => 'Order deleted successfully']);
        } else {
            echo json_encode(['error' => 'Order ID not provided']);
        }
        break;

    default:
        echo json_encode(['error' => 'Invalid request method']);
        break;
}

?>