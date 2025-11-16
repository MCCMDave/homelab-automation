# ⚡ Power Savings Tracker

**[🇩🇪 Deutsche Version](README_DE.md)** | 🇬🇧 English Version

---

A simple Python tool to calculate electricity cost savings from solar power generation.

---

## 📖 Description

This tool calculates electricity cost savings based on solar power generation (kWh) and stores the history in a CSV file.

---

## ✨ Features

- ✅ Calculate savings based on current electricity price
- ✅ Automatic CSV export with history
- ✅ Header creation for new files
- ✅ Date stamp for each measurement
- ✅ Input validation (numbers only)
- ✅ Error handling for invalid inputs

---

## 🚀 Installation & Usage

### Requirements:
- Python 3.7 or higher

### Execution:
```bash
python power_savings_tracker.py
```

### Usage:
1. Start program
2. Enter generated kWh
3. Savings are displayed
4. Data saved to `historie.csv`
5. Press ENTER to exit

---

## 📊 Example Output

```
How many kWh were generated? 12.5

On 16.11.25 the electricity cost savings are: 3.65€

Press ENTER to close the window.
```

---

## 📁 File Structure

### Generated Files:
- **historie.csv** - Stores all measurements with date

### CSV Format:
```csv
Date; kWh; Savings in €
16.11.25; 12.50; 3.65
17.11.25; 15.20; 4.43
```

---

## ⚙️ Configuration

### Adjust Electricity Price:
```python
# Line 5 in power_savings_tracker.py:
price = 0.2916  # Current electricity price in €/kWh
```

**Current Price:** 0.2916 €/kWh (as of November 2025)

---

## 🛠️ Technical Details

### Modules Used:
- `datetime` - Date management
- `os` - Filesystem checks

### How It Works:
1. Get current date
2. kWh input from user
3. Calculate savings (kWh × price)
4. Check if CSV exists/empty
5. Add header if needed
6. Append data

---

## 📈 Future Enhancements

**Possible Improvements:**
- [ ] Monthly/yearly statistics
- [ ] Graphical analysis (matplotlib)
- [ ] Automatic data retrieval from inverter
- [ ] Comparison with previous months
- [ ] PDF report export
- [ ] Web interface with Flask

---

## 🏠 Homelab Integration

**Current:** Manual input  
**Planned:** Automatic retrieval from inverter via API

**My Setup:**
- Solar panels on roof
- Inverter with network connectivity
- Raspberry Pi 5 as homelab server

---

## 💡 Learning Journey

This tool was one of my first Python projects while learning:
- Input/Output
- Variables & data types
- File operations
- Error handling
- CSV export

**Part of:** [Python Learning Journey](https://github.com/MCCMDave/python-learning)

---

## 🔗 Related Projects

- [Service Monitor](../service-monitor/) - Homelab service monitoring
- [Python Learning](https://github.com/MCCMDave/python-learning) - My learning journey

---

## 👨‍💻 Author

**David Vaupel**  
Homelab Enthusiast | Python Learner | Linux Essentials Certified

---

**Status:** ✅ Production-Ready | In Daily Use  
**Version:** 1.0  
**Last Updated:** November 2025
