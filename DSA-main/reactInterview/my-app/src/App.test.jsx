import { render, screen, fireEvent } from "@testing-library/react";
import { test, expect, vi } from "vitest";
import App from "./App";
import { mockApi } from "./api";

// Mock api.js
vi.mock("./api", () => ({
  mockApi: {
    fetchMock: vi.fn(),
  },
}));

test("loads and displays data when button is clicked", async () => {
  const mockData = [
    { id: 1, name: "Laptop" },
    { id: 2, name: "Mobile" },
  ];

  mockApi.fetchMock.mockResolvedValue(mockData);

  render(<App />);

  const button = screen.getByText("Load Data");

  fireEvent.click(button);

  expect(mockApi.fetchMock).toHaveBeenCalledWith(
    "Electronic"
  );

  expect(
    await screen.findByText("Laptop")
  ).toBeTruthy();

  expect(
    await screen.findByText("Mobile")
  ).toBeTruthy();
});