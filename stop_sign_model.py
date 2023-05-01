import torch
import torch.nn as nn
import torch.nn.functional as F

class StopSignModel(torch.nn.Module):
	def __init__(self):
		super(StopSignModel, self).__init__()
		self.conv1 = nn.Conv2d(1, 32, kernel_size = 5, padding = 2)
		self.conv2 = nn.Conv2d(32, 64, kernel_size = 5, padding = 2)
		self.conv3 = nn.Conv2d(64, 128, kernel_size = 5, padding = 2)
		self.dropout = nn.Dropout2d(p = 0.5)
		self.pool = nn.MaxPool2d(kernel_size = 2)
		self.convT1 = nn.ConvTranspose2d(128, 64, kernel_size = 5, stride = 2, padding = 2, output_padding = 1)
		self.convT2 = nn.ConvTranspose2d(64, 32, kernel_size = 5, stride = 2, padding = 2, output_padding = 1)
		self.convT3 = nn.ConvTranspose2d(32, 1, kernel_size = 5, stride = 2, padding = 2, output_padding = 1)
		self.activation = nn.ReLU()
		self.last_activation = nn.Sigmoid()

	def forward(self, input):
		x = self.activation(self.pool(self.conv1(input)))
		x1 = self.activation(self.pool(self.conv2(x)))
		x2 = self.activation(self.pool(self.conv3(x1)))
		x3 = self.dropout(x2)
		x4 = self.activation(self.pool(self.convT1(x3)))
		x5 = self.activation(self.pool(self.convT2(x4)))
		x6 = self.activation(self.pool(self.convT3(x5)))
		x7 = self.dropout(x6)
		out = self.last_activation(x7)

		return out
