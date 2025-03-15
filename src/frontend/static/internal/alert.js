if (typeof ModernAlerts === "undefined") {
    class ModernAlerts {
        constructor() {
            if (!document.getElementById("modern-alerts-container")) {
                const container = document.createElement("div");
                container.id = "modern-alerts-container";
                document.body.appendChild(container);

                this.injectStyles();
            }

            this.container = document.getElementById("modern-alerts-container");
        }

        injectStyles() {
            const styleElement = document.createElement("style");
            const css = String.raw;

            styleElement.textContent = css`
                #modern-alerts-container {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    pointer-events: none;
                    z-index: 9999;
                }

                .modern-alert {
                    border: 1px solid #e7e5e5;
                    background: white;
                    border-radius: 3px;
                    width: 340px;
                    max-width: 95%;
                    display: flex;
                    flex-direction: column;
                    position: relative;
                    pointer-events: auto;
                    animation: alertIn 0.25s cubic-bezier(0.21, 1.02, 0.73, 1) forwards;
                    transform: translateY(10px);
                    opacity: 0;
                    overflow: hidden;
                }

                @keyframes alertIn {
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                @keyframes alertOut {
                    to {
                        opacity: 0;
                        transform: translateY(-10px);
                    }
                }

                .modern-alert-backdrop {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(255, 255, 255, 0.35);
                    backdrop-filter: blur(3px);
                    z-index: 9998;
                    opacity: 0;
                    animation: backdropIn 0.2s ease forwards;
                }

                @keyframes backdropIn {
                    to {
                        opacity: 1;
                    }
                }

                @keyframes backdropOut {
                    to {
                        opacity: 0;
                    }
                }

                .modern-alert-header {
                    display: flex;
                    align-items: center;
                    padding: 16px 16px 12px;
                    border-bottom: 1px solid #e7e5e5;
                }

                .modern-alert-icon {
                    width: 32px;
                    height: 32px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 8px;
                    flex-shrink: 0;
                }

                .modern-alert-icon svg {
                    width: 20px;
                    height: 20px;
                }

                .modern-alert-title {
                    font-size: 16px;
                    font-weight: 600;
                    color: #888;
                    flex-grow: 1;
                    padding-top: 1px;
                }

                .modern-alert-body {
                    padding: 12px 16px;
                    font-size: 14px;
                    font-weight: 400;
                    color: #747474;
                    line-height: 1.4;
                }

                .modern-alert-actions {
                    display: flex;
                    justify-content: flex-end;
                    padding: 8px 16px 16px;
                }

                .modern-alert-button {
                    padding: 8px 16px;
                    border: none;
                    border-radius: 2px;
                    font-size: 14px;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.1s ease;
                }

                /* Cores específicas */
                .modern-alert-success .modern-alert-icon {
                    background: rgba(72, 187, 120, 0.15);
                    color: #48bb78;
                }

                .modern-alert-success .modern-alert-button {
                    border: 1px solid #e7e5e5;
                    color: #48bb78;
                }

                .modern-alert-error .modern-alert-icon {
                    background: rgba(245, 101, 101, 0.15);
                    color: #f56565;
                }

                .modern-alert-error .modern-alert-button {
                    border: 1px solid #e7e5e5;
                    color: #f56565;
                }

                .modern-alert-warning .modern-alert-icon {
                    background: rgba(237, 137, 54, 0.15);
                    color: #ed8936;
                }

                .modern-alert-warning .modern-alert-button {
                    border: 1px solid #e7e5e5;
                    color: #ed8936;
                }

                .modern-alert-info .modern-alert-icon {
                    background: rgba(66, 153, 225, 0.15);
                    color: #4299e1;
                }

                .modern-alert-info .modern-alert-button {
                    border: 1px solid #e7e5e5;
                    color: #4299e1;
                }

                /* Barra de progresso para auto-close */
                .modern-alert-progress {
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    height: 3px;
                    background: currentColor;
                    opacity: 0.5;
                }
            `;
            document.head.appendChild(styleElement);
        }

        // Criar um alerta
        createAlert(type, message, title, timer) {
            const backdrop = document.createElement("div");
            backdrop.className = "modern-alert-backdrop";
            document.body.appendChild(backdrop);

            const alert = document.createElement("div");
            alert.className = `modern-alert modern-alert-${type}`;

            let iconSvg;
            switch (type) {
                case "success":
                    iconSvg =
                        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>';
                    break;
                case "error":
                    iconSvg =
                        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>';
                    break;
                case "warning":
                    iconSvg =
                        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>';
                    break;
                case "info":
                    iconSvg =
                        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>';
                    break;
            }

            alert.innerHTML = `
                <div class="modern-alert-header">
                    <div class="modern-alert-icon">${iconSvg}</div>
                    <div class="modern-alert-title">${title}</div>
                </div>
                <div class="modern-alert-body">${message}</div>
                <div class="modern-alert-actions">
                    <button class="modern-alert-button">OK</button>
                </div>
            `;

            if (timer) {
                const progress = document.createElement("div");
                progress.className = "modern-alert-progress";
                alert.appendChild(progress);

                progress.style.transition = `width ${timer}ms linear`;
                setTimeout(() => (progress.style.width = "100%"), 10);
            }

            this.container.appendChild(alert);

            const closeAlert = () => {
                alert.style.animation = "alertOut 0.2s forwards";
                backdrop.style.animation = "backdropOut 0.2s forwards";

                setTimeout(() => {
                    if (this.container.contains(alert)) {
                        this.container.removeChild(alert);
                    }
                    if (document.body.contains(backdrop)) {
                        document.body.removeChild(backdrop);
                    }
                }, 200);
            };

            const button = alert.querySelector(".modern-alert-button");
            button.addEventListener("click", closeAlert);

            if (timer) {
                setTimeout(closeAlert, timer);
            }

            backdrop.addEventListener("click", closeAlert);

            return new Promise((resolve) => {
                button.addEventListener("click", () => resolve(true));
            });
        }

        success(message, title = "Sucesso", timer = 0) {
            return this.createAlert("success", message, title, timer);
        }

        error(message, title = "Erro", timer = 0) {
            return this.createAlert("error", message, title, timer);
        }

        warning(message, title = "Atenção", timer = 0) {
            return this.createAlert("warning", message, title, timer);
        }

        info(message, title = "Informação", timer = 0) {
            return this.createAlert("info", message, title, timer);
        }
    }

    window.Alert = new ModernAlerts();
}
