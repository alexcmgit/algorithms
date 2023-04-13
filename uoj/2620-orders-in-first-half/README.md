<p><a href="https://www.beecrowd.com.br/repository/UOJ_2620_en.html">beecrowd.com.br/repository/UOJ_2620_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2620 </span>
                                    <h1>Orders in First Half</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>The company's financial audit is asking us for a report for the first half of 2016. Then display the customers name and order number for customers who placed orders in the first half of 2016.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>customers</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>street</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>city</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>state</td>
                                  <td>char (2)</td>
                                </tr>
                                <tr>
                                  <td>credit_limit</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>orders</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>orders_date</td>
                              <td>date (ISO/YMD)</td>
                            </tr>
                            <tr>
                              <td>id_customers (FK)</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>customers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                      <td><strong>state</strong></td>
                      <td><strong>credit_limit</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Nicolas Diogo Cardoso</td>
                      <td>Acesso Um</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>475</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Cecília Olivia Rodrigues</td>
                      <td>Rua Sizuka Usuy</td>
                      <td>Cianorte</td>
                      <td>PR</td>
                      <td>3170</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Augusto Fernando Carlos Eduardo Cardoso</td>
                      <td>Rua Baldomiro Koerich</td>
                      <td>Palhoça</td>
                      <td>SC</td>
                      <td>1067</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Nicolas Diogo Cardoso</td>
                      <td>Acesso Um</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>475</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Sabrina Heloisa Gabriela Barros</td>
                      <td>Rua Engenheiro Tito Marques Fernandes</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                      <td>4312</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Joaquim Diego Lorenzo Araújo</td>
                      <td>Rua Vitorino</td>
                      <td>Novo Hamburgo</td>
                      <td>RS</td>
                      <td>2314</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>orders</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>orders_date</strong></td>
                  <td><strong>id_customers</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>2016-05-13</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>2016-01-12</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>2016-04-18</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>2016-09-07</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>2016-02-13</td>
                  <td>6</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>2016-08-05</td>
                  <td>3</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>id</strong></td>
        </tr>
        <tr>
          <td>Augusto Fernando Carlos Eduardo Cardoso</td>
          <td>1</td>
        </tr>
        <tr>
          <td>Cecília Olivia Rodrigues</td>
          <td>2</td>
        </tr>
        <tr>
          <td>Sabrina Heloisa Gabriela Barros</td>
          <td>3</td>
        </tr>
        <tr>
          <td>Joaquim Diego Lorenzo Araújo</td>
          <td>5</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>